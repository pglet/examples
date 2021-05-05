# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page gap=20"
  pglet_send "add
stack horizontal
  icon name=ChangeEntitlements color=SlateGray
  icon name=shop color=Khaki
  icon name=TrainSolid
stack horizontal verticalAlign=center
  icon name=BlockedSite color=Maroon size=25px
  icon name=settings color=SlateBlue size=50px
  icon name=save size=100px
"
}

pglet_app "index" "main"