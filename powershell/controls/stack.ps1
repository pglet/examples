Import-Module pglet

Connect-PgletApp -Name "pglet-stack" -ScriptBlock {
    $ErrorActionPreference = 'stop'
  
    $pglet_page.horizontalAlign = 'Stretch'
    $pglet_page.update()
  
    $bgColor = '#ddddee'
  
    function items($count) {
      $items = @()
      for($i = 1; $i -le $count; $i++) {
        $items += (Text -Value "$i" -Align Center -VerticalAlign Center -Width 30 -Height 30 -BgColor CyanBlue10 -Color White -Padding 5)
      }
      return $items
    }  
  
    function createHorizontalStack($horizAlign) {
      Stack -Controls @(
        Text -Value $horizAlign
        Stack -Horizontal -HorizontalAlign $horizAlign -VerticalAlign Center -Gap 20 -BgColor $bgColor -Controls (items 3)
      )
    }
  
    function createVerticalStack($vertAlign, $horizAlign) {
      Stack -Width '20%' -Controls @(
        Text -Value $vertAlign
        Stack -VerticalAlign $vertAlign -HorizontalAlign Center -Height 300 -Gap 20 -BgColor $bgColor -Controls (items 3)
      )
    }
  
    # Gap, padding
    $spacingStack = Stack -Horizontal -BgColor $bgColor -Gap 0 -Controls (items 5)
    $gapSlider = Slider "Gap between items" -Min 0 -Max 50 -Step 1 -Value 0 -ShowValue -OnChange {
      $spacingStack.gap = $gapSlider.value
      $spacingStack.update()
    }
    $paddingSlider = Slider "Stack padding" -Min 0 -Max 50 -Step 1 -Value 0 -ShowValue -OnChange {
      $spacingStack.padding = $paddingSlider.value
      $spacingStack.update()
    }
  
    $pglet_page.add(
      (Text "Horizontal stack - Gap and Padding" -Size xLarge),
      $gapSlider,
      $paddingSlider,
      $spacingStack
    )
  
    # Wrapping
    $wrapStack = Stack -Horizontal -Wrap -BgColor $bgColor -Gap 20 -Controls (items 10)
    $wrapSlider = Slider "Change the stack width to see how child items wrap onto multiple rows:" `
        -Min 0 -Max 100 -Step 10 -Value 100 -Width '100%' -ShowValue -ValueFormat '{value}%' -OnChange {
      $wrapStack.width = "$($wrapSlider.value)%"
      $wrapStack.update()
    }
    
    $pglet_page.add(
      (Text "Horizontal stack - Wrapping" -Size xLarge),
      $wrapSlider,
      $wrapStack,
  
      (Text "Horizontal stack - Horizontal Alignments" -Size xLarge),
      (createHorizontalStack 'Start'),
      (createHorizontalStack 'Center'),
      (createHorizontalStack 'End'),
      (createHorizontalStack 'SpaceBetween'),
      (createHorizontalStack 'SpaceAround'),
      (createHorizontalStack 'SpaceEvenly'),
  
      (Text "Horizontal stack - Vertical Alignments" -Size xLarge),
      (Text "Start"),
      (Stack -Horizontal -VerticalAlign 'Start' -Height 100 -BgColor $bgColor -Gap 20 -Controls (items 3)),
      (Text "Center"),
      (Stack -Horizontal -VerticalAlign 'Center' -Height 100 -BgColor $bgColor -Gap 20 -Controls (items 3)),
      (Text "End"),
      (Stack -Horizontal -VerticalAlign 'End' -Height 100 -BgColor $bgColor -Gap 20 -Controls (items 3))
    )
  
    # Vertical stack
    $vertStacks = Stack -Horizontal -HorizontalAlign SpaceBetween -Width '100%' -Controls @(
      (createVerticalStack 'Start'),
      (createVerticalStack 'Center'),
      (createVerticalStack 'End'),
      (createVerticalStack 'SpaceBetween'),
      (createVerticalStack 'SpaceAround'),
      (createVerticalStack 'SpaceEvenly')
    )
  
    $pglet_page.add(
      (Text "Vertical stack - Vertical Alignments" -Size xLarge),
      $vertStacks
    )
  
    # Stack submit
    $form1 = Stack -Padding 10 -width '50%' -Border '2px solid #eee' -BorderRadius 5 -Controls @(
      Text "Pressing ENTER inside the stack will fire 'submit' event."
      TextBox "First name"
      TextBox "Last name"
    ) -OnSubmit {
      $form1.controls.insert(0, (Message "Form has been submitted!" -Type Success -Dismiss))
      $form1.update()
    }
    $pglet_page.add(
      (Text "Stack with Submit event" -Size xLarge),
      $form1
    )
  }