# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=30"
  pglet_send "add
    stack
      text value='Basic dropdown' size=xLarge
      dropdown
        option key=Red
        option key=Green
        option key=Blue

    stack
      text value='Dropdown with label and placeholder' size=xLarge
      dropdown label=Color placeholder='What\'s your favourite color?'
        option key=Red
        option key=Green
        option key=Blue
  "
}

pglet_app "index" "main"