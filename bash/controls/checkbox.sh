# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "add
    checkbox label='Unchecked checkbox'
    checkbox label='Checked checkbox' value='true'
    checkbox disabled label='Disabled checkbox'
    checkbox label='Checkbox with rendered boxSide=\'end\'' boxSide=end
  "
}

pglet_app "index" "main"