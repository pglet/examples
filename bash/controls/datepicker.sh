# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
    datepicker label='Start date' value='10/02/2021'
    datepicker label='End date'
    datepicker allowTextInput label='Allow text input'
    datepicker allowTextInput label='Allow text input with placeholder' placeholder='Select date...' width='30%'
    datepicker value='01/01/2012' allowTextInput label='Required' placeholder='Select date...' width='30%'
  "
}

pglet_app "index" "main"