# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
text value='Line chart' size=xlarge
lineChart legend tooltips xtype=date yticks=10 ymax=100 yformat='{y}%' width='100%' height=300
  data legend='Line A'
    p x='2020-03-03T00:00:00.000Z' y=10
    p x='2020-03-03T10:00:00.000Z' y=50
    p x='2020-03-03T11:00:00.000Z' y=70
  data legend='Line B'
    p x='2020-03-03T00:00:00.000Z' y=30
    p x='2020-03-04T00:00:00.000Z' y=20
    p x='2020-03-05T00:00:00.000Z' y=90
"
}

pglet_app "index" "main"