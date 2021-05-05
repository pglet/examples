# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
text value='Pie chart' size=xlarge

pieChart width='100%' innerRadius=40 innerValue=42
  data
    p color='yellow' legend='' value=20
    p color='green' legend='' value=30

pieChart legend tooltips width='100%' innerRadius=40 innerValue=42
  data
    p legend='Free space' value=20 tooltip='20%'
    p legend='Total space' value=50 tooltip='50%'
    p legend='Reserved space' value=30 tooltip='30%'
    p legend='A' value=1 tooltip='20%'
    p legend='B' value=2 tooltip='50%'
    p legend='C' value=3 tooltip='30%'"
}

pglet_app "index" "main"