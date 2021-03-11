Import-Module pglet

$userName = $env:UserName
$compName = $env:ComputerName
$totalRam = (Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property capacity -Sum).Sum / 1024 / 1024

Connect-PgletPage -Name "pglet-demo/*" -web

Invoke-Pglet "set page title='Task Manager' padding=10px"

Invoke-Pglet "add
text id=title value='Task Manager' size=xLarge
tabs id=computers width='100%'
  tab text=$compName
    stack id=$compName gap=20
"

$tabId = "computers:$compName"

Invoke-Pglet "clean $tabId"

Invoke-Pglet "add to=$tabId
stack horizontal gap=20
  stack width='50%'
    grid compact=false shimmerLines=5 selection=single preserveSelection=true headerVisible=true
      columns
        column resizable sortable fieldName='name' name='Process name' maxWidth=100
        column resizable sortable=number fieldName='pid' name='PID' maxWidth=100
        column resizable sortable sorted=desc fieldName='cpu_display' sortField=cpu name='CPU %' maxWidth=100
        column resizable sortable fieldName='path' name='Path'
      items id=gridItems
  stack width='40%'
    text value='CPU, %' size=large
    lineChart tooltips xtype=date yticks=5 ymax=100 yformat='{y}%' height=250
      data id=cpu_chart legend='CPU'
    text value='RAM, MB' size=large
    lineChart tooltips xtype=date yticks=5 ymax=$totalRam height=250
      data id=ram_chart legend='RAM'
"

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

# Generate 30 empty values for the last minute to initially fill charts
$points=@()
for($i = -30; $i -lt 0; $i++) {
  $d=(Get-Date).AddSeconds($i*2)
  $points += "p x='$d' y=0"
}

# Init CPU chart with "past" data
$cpuChartId="$($tabId):cpu_chart"
Invoke-Pglet "addf to=$cpuChartId `n$($points -join "`n")"

# Init RAM chart with "past" data
$ramChartId="$($tabId):ram_chart"
Invoke-Pglet "addf to=$ramChartId `n$($points -join "`n")"

# Main update loop
while($true) {

  # update top processes
  $cmd = "replace to=$($tabId):gridItems`n"
  $cmd += (getTopProcesses 10 |
    ForEach-Object { "item id=$($_.PID) pid=$($_.PID) name='$($_.InstanceName)' cpu=$($_.CPU) cpu_display='$($_.CPU)%' path='$($_.Path -replace '\\', '\\')'" }) -join "`n"
  Invoke-Pglet $cmd | Out-Null

  $d=(Get-Date)

  # Update CPU load
  $cpuLoad = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue.ToString("#,0.00")
  Invoke-Pglet "addf to=$cpuChartId trim=30 p x='$d' y=$cpuLoad"

  # Update RAM load
  $availRam = (Get-Counter '\Memory\Available MBytes').CounterSamples.CookedValue
  $usedRam = $totalRam - $availRam
  $usedRamGB = ($usedRam/1024).ToString("#,0.00")
  Invoke-Pglet "addf to=$ramChartId trim=30 p x='$d' y=$usedRam ytooltip='$usedRamGB GB'"

  Start-Sleep -s 2
}
