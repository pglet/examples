# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=20"
  pglet_send "add
link url='http://google.com' value='Visit Google' newWindow
link value='Link without URL' size=large
link url='http://google.com' value='Cannot visit this link' disabled
  "
}

pglet_app "index" "main"