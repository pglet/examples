# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
text value='Horizontal Bar Chart' size=xlarge
barChart dataMode=fraction width='50%' tooltips
  data
    p legend='C:' x=20 y=250 xtooltip='20%' ytooltip='250 GB'
    p legend='D:' x=50 y=250 xtooltip='50%' color=yellow
    p legend='E:' x=30 y=250 xtooltip='30%'
"
}

pglet_app "index" "main"