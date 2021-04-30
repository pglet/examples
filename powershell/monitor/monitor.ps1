Import-Module pglet

function getTopProcesses($maxCount) {
  $procIDs = @{}
  (Get-Counter "\Process(*)\ID Process" -ErrorAction SilentlyContinue).CounterSamples |
    ForEach-Object { $procIDs[($_.Path -replace "\\id process$","\% Processor Time")] = $_.CookedValue }

  $CpuCores = (Get-CimInstance -ClassName Win32_ComputerSystem).NumberOfLogicalProcessors
  return (Get-Counter "\Process(*)\% Processor Time" -ErrorAction SilentlyContinue).CounterSamples |
    Where-Object {$_.InstanceName -notmatch "^(idle|_total|system)$"} |
    Sort-Object "CookedValue" -descending |
    Select-Object -first $maxCount `
        @{Name="PID";Expression={$procIDs[$_.Path]}},
        @{Name="Path";Expression={(Get-Process -id $procIDs[$_.Path]).Path}},
        InstanceName,
        @{Name="CPU";Expression={[Decimal]::Round(($_.CookedValue / $CpuCores), 2)}}
}

function getEmptyData() {
    # Generate 30 empty values for the last minute to initially fill charts
    $points=@()
    for($i = -30; $i -lt 0; $i++) {
        $d=(Get-Date).AddSeconds($i*2)
        $points += LineChartDataPoint -X $d -Y 0
    }
    return $points
}

$userName = $env:UserName
$compName = $env:ComputerName
$totalRam = (Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property capacity -Sum).Sum / 1024 / 1024

$page = Connect-PgletPage -Name "ps-monitor"
$page.title = 'Task Manager'
$page.padding = '10px'
$page.update()

$tab = Tab -Id $compName -Text $compName

$page.add(
    (Text -Id 'title' -Value 'Task Manager' -Size xLarge),
    (Tabs -Id 'computers' -Width '100%' -TabItems @(
        $tab
)))

$tab.clean()

$proc_grid = Grid -ShimmerLines 5 -SelectionMode Single -PreserveSelection -HeaderVisible -KeyFieldName 'PID' -Columns @(
  GridColumn -Resizable -Sortable 'string' -FieldName 'name' -Name 'Process name' -MaxWidth 100
  GridColumn -Resizable -Sortable 'number' -FieldName 'pid' -Name 'PID' -MaxWidth 100
  GridColumn -Resizable -Sortable 'string' -FieldName 'cpu_display' -SortField 'cpu' -Name 'CPU %' -MaxWidth 100
  GridColumn -Resizable -Sortable 'string' -FieldName 'path' -Name 'Path'
)

$cpu_chart = LineChartData -Legend 'CPU' -Points (getEmptyData)
$ram_chart = LineChartData -Legend 'RAM' -Points (getEmptyData)

$stack = Stack -Horizontal -Controls @(
    Stack -Width '50%' -Controls @(
        $proc_grid
    )
    Stack -Width '40%' -Controls @(
        Text -Value 'CPU, %' -Size Large
        LineChart -Tooltips -XType Date -YTicks 5 -YMax 100 -YFormat '{y}%' -Height 250 -Lines @(
            $cpu_chart
        )
        Text -Value 'RAM, MB' -Size Large
        LineChart -Tooltips -XType Date -YTicks 5 -YMax $totalRam -Height 250 -Lines @(
            $ram_chart
        )
    )
)

$tab.controls.add($stack)
$tab.update()

# Main update loop
while($true) {

  $proc_grid.items = getTopProcesses 10 | ForEach-Object {
    @{
      pid = $_.PID
      name = $_.InstanceName
      cpu = $_.CPU
      cpu_display = "$($_.CPU)%"
      path = $_.Path
    }
  }

  $d=(Get-Date)

  # Update CPU load
  $cpuLoad = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue.ToString("#,0.00")
  $cpu_chart.points.removeAt(0)
  $cpu_chart.points.add((LineChartDataPoint -X $d -Y $cpuLoad))

  # Update RAM load
  $availRam = (Get-Counter '\Memory\Available MBytes').CounterSamples.CookedValue
  $usedRam = $totalRam - $availRam
  $usedRamGB = ($usedRam/1024).ToString("#,0.00")
  $ram_chart.points.removeAt(0)
  $ram_chart.points.add((LineChartDataPoint -X $d -Y $usedRam -YTooltip "$usedRamGB GB"))

  $page.update()

  Start-Sleep -s 2
}
