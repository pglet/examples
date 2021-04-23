# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "add
stack gap=30

  stack
    text value='Default SearchBox' size=large
    searchbox
  
  stack
    text value='Underlined SearchBox' size=large
    searchbox underlined placeholder='Search files and folders'

  stack
    text value='Disable SearchBox' size=large
    searchbox disabled placeholder='Search something...'
    searchbox underlined disabled placeholder='Search something...'

  stack
    text value='SearchBox with custom icon' size=large
    searchbox placeholder='Filter something by' icon=Filter iconColor=red
  "
}

pglet_app "index" "main"