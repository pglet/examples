. pglet.sh

function main() {
  pglet_send "clean"
  pglet_send "add text value='Hello, world!'"
}

pglet_app "hello-app" main