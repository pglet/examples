# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=30"
  pglet_send "add
    text value='Vertical chart with textual x axis' size=xlarge
    verticalBarChart tooltips legend=false width='50%' height=300 yticks=5 barWidth1=20 yFormat='{y}%'
      data
        p id=rdp x=Red y=20 color=MediumOrchid legend=Red ytooltip='20%'
        p x=Green y=50 color=LimeGreen legend=Green ytooltip='50%'
        p x=Blue y=20 color=LightSkyBlue legend=Blue ytooltip='30%'

    text value='Vertical chart with numeric x axis' size=xlarge
    verticalBarChart tooltips legend=false width='100%' xtype=number1 height=400 ymin=50 ymax=100 yticks=5 barWidth=20
      data id=d1
  "

  for ((i=21;i<=40;i++)); do
    pglet_send "setf rdp y=$i"
    sleep 0.01
  done

  for ((i=0;i<=100;i++)); do
    y=$RANDOM
    let "y %= 100"
    pglet_send "addf p to=d1 trim=30 x=$i y=$y"
    sleep 0.05
  done  
}

pglet_app "index" "main"