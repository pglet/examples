# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function text() {
  pglet_send "
add
text value=Squares size=large
stack horizontal
  text value='left top' align=left verticalAlign=top width=100 height=100 bgColor=Salmon color=white padding=5
  text value='center top' size=large align=center verticalAlign=top width=100 height=100 bgColor=Salmon color=white padding=5 border='1px solid #555'
  text value='right top' align=right verticalAlign=top width=100 height=100 bgColor=Salmon color=white padding=5 border='2px solid #555'
stack horizontal
  text value='left center' align=left verticalAlign=center width=100 height=100 bgColor=PaleGoldenrod padding=5
  text value='center center' size=large align=center verticalAlign=center width=100 height=100 bgColor=PaleGoldenrod padding=5 padding=5  border='1px solid #555'
  text value='right center' align=right verticalAlign=center width=100 height=100 bgColor=PaleGoldenrod padding=5  border='2px solid #555'
stack horizontal
  text value='left bottom' align=left verticalAlign=bottom width=6rem height=6rem bgColor=PaleGreen padding=5
  text value='center bottom' size=large align=center verticalAlign=bottom width=6rem height=6rem bgColor=PaleGreen padding=5 padding=5 border='1px solid #555'
  text value='right bottom' align=right verticalAlign=bottom width=6rem height=6rem bgColor=PaleGreen padding=5 border='2px solid #555'
text value=Circles size=large
stack horizontal
  text value='regular' align=center verticalAlign=center width=100px height=100px bgColor=Salmon color=white borderRadius=50
  text bold italic value='bold italic' align=center verticalAlign=center width=100 height=100 bgColor=PaleGoldenrod borderRadius=50 border='1px solid #555'
  text bold value='bold' align=center verticalAlign=center width=100 height=100 bgColor=PaleGreen color='#555' borderRadius=50 border='2px solid #555'
text value=Markdown size=large
stack
  text value='Code sample' size=xlarge
  text markdown value='\`\`\`powershell\n\$i = 0\nInvoke-Pglet ""clean page""\n\`\`\`'
text value=Quotes size=large
stack
  text value='""line 1""'
  text value='\'line 2\''
  text value=""'line 3'""

"

echo '
  text value='"line 1"'
  text value='\'line 2\''
'

}

pglet_app "index" "text"