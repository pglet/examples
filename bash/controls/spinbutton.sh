# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=20"
  pglet_send "add
spinButton label='Basic SpinButton:' min=0 max=100 step=1 value=0
spinButton disabled label='Disabled SpinButton:' min=0 max=100 step=1 value=0
spinButton icon=IncreaseIndentLegacy label='SpinButton with icon:' min=0 max=100 step=1 value=0
  "
}

pglet_app "index" "main"