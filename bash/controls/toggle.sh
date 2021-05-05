# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
    toggle label='Enabled and checked' value='true'
    toggle label='Enabled and unchecked'
    toggle disabled label='Disabled and checked' value='true'
    toggle disabled label='Disabled and unchecked'
    toggle inline label='With inline label' onText=On offText=Off
    toggle disabled inline label='Disabled with inline label' onText=On offText=Off
    toggle inline label='With inline label and without onText and offText'
    toggle disabled inline label='Disabled with inline label and without onText and offText'  
  "
}

pglet_app "index" "main"