# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
  stack width='50%'
    slider label='Default slider'
    slider label='Default disabled slider' disabled
    slider label='Slider with value' showValue value=4
    slider label='Slider with formatted value' showValue valueFormat='{value}%'
    slider showValue label='Origin from zero' min='-5' max=15 step=1 value=-2
  stack horizontal height=200px
    slider vertical label='Default slider'
    slider vertical label='Default disabled slider' disabled
    slider vertical label='Slider with value' showValue value=4
    slider vertical label='Slider with formatted value' showValue valueFormat='{value}%'
    slider vertical showValue label='Origin from zero' min='-5' max=15 step=1 value=-2 
  "
}

pglet_app "index" "main"