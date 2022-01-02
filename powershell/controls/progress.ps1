Import-Module pglet

Connect-PgletApp -Name "pglet-progress" -ScriptBlock {
    $ErrorActionPreference = 'stop'
  
    $page = $pglet_page
  
    $controls = @(
      Text "Indeterminate Progress" -Size xLarge
      Progress -Label "Operation progress" -Description "Doing something indefinite..." -Width "30%"
    )
    
    $page.add($controls)
  
    $prog1 = Progress -Label "Copying file1.txt to file2.txt" -Width "30%" -BarHeight 4
    $page.add($prog1)
  
    for($i = 0; $i -lt 101; $i=$i+10) {
      $prog1.value = $i
      $prog1.update()
      Start-Sleep -Milliseconds 500
    }
  
    $prog2 = Progress -Label "Provisioning your account" -Value 0 -Width "30%"
    $page.add($prog2)
  
    $prog2.description = "Preparing environment..."
    $prog2.value = 50
    $prog2.update()
    Start-Sleep -Seconds 2
  
    $prog2.description = "Collecting information..."
    $prog2.value = 100
    $prog2.update()
    Start-Sleep -Seconds 2
  
    $prog2.value = $null
    $prog2.update()  
  }