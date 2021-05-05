# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
iframe src='https://pglet.io' width='100%' height=300 border='2px solid #eee'
"
}

pglet_app "index" "main"