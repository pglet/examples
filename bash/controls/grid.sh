# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "
add
stack gap=30

  stack width='50%'
    text value='Basic grid' size=large
    grid
      columns
        column name='First name' fieldName='first_name'
        column name='Last name' fieldName='last_name'
        column name='Age' fieldName='age'
      items
        item first_name='John' last_name='Smith' age=30
        item first_name='Samantha' last_name='Fox' age=43
        item first_name='Alice' last_name='Brown' age=25

  stack
    text value='Sortable grid with resizable columns and selectable rows' size=large
    grid selection=single preserveSelection
      columns
        column resizable sortable name='First name' fieldName='first_name'
        column resizable sortable sorted=asc name='Last name' fieldName='last_name'
        column resizable sortable=number name='Age' fieldName='age'
      items
        item first_name='Alice' last_name='Brown' age=25
        item first_name='Samantha' last_name='Fox' age=43
        item first_name='John' last_name='Smith' age=30

  stack
    text value='Compact grid with no header and multiple selection' size=large
    grid compact headerVisible=false selection=multiple
      columns
        column maxWidth=100 fieldName='first_name'
        column maxWidth=100 fieldName='last_name'
        column maxWidth=100 fieldName='age'
      items
        item first_name='John' last_name='Smith' age=30
        item first_name='Samantha' last_name='Fox' age=43
        item first_name='Alice' last_name='Brown' age=25

  stack
    text value='Grid with template columns and auto-generated items' size=large
    grid id=grid1 shimmerLines=5 selection=single preserveSelection
      columns
        column onClick name='File Type' icon=Page iconOnly fieldName='iconName' minWidth=20 maxWidth=20
          icon name=Package size=16
        column resizable sortable name='Name' fieldName='name'
          text value='{name}'
        column resizable name='Write' fieldName='write'
          stack horizontal height='100%' verticalAlign=center
            checkbox value='{write}'
        column resizable name='Color' fieldName='read'
          dropdown value='{color}' data='{key}' placeholder=select
            option key=red text='Red'
            option key=green text='Green'
            option key=blue text='Blue'
        column resizable sortable name='Description' fieldName='description'
          textbox value='{description}'
        column sortable=number name='Action' fieldName='key' minWidth=150
          stack horizontal height='100%' verticalAlign=center
            link url='{key}' value='{iconName}' visible=false
            link url='{key}' value='{name}' visible=false
            button icon='Edit' title='Edit todo' width=16 height=16 visible=true data='{key}'
            button icon='Delete' iconColor=red title='Delete todo' width=16 height=16 visible=true data='{key}'
      items id=items
  "

  # small delay before adding grid items, so you can see a shimmer
  sleep 5

  total_items=10
  cmd="replace to=grid1:items"
  for ((i=1;i<=$total_items;i++)); do
    cmd="$cmd
    item key=item$i name='Item $i' iconName='ItemIcon$i'"
  done
  pglet_send "$cmd"
}

pglet_app "index" "main"