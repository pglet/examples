# This example uses Pglet for rendering web UI.
# Read more about Pglet at https://pglet.io/docs/

# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

# tasks and their statuses
next_task_id=0
task_ids=()
task_completed=()
task_names=()

# current tasks view
current_view=""
view_task_ids=()
active_tasks=0

function update_tasks_view() {
  # $1 - 'true' - completed tasks, 'false' - active tasks or '' - all tasks
  view_task_ids=()
  active_tasks=0
  cmd="replace to=tasks"
  for (( i = 0; i < ${#task_ids[@]}; ++i )); do
    if [[ "${task_completed[i]}" == "false" ]]; then
      ((active_tasks=active_tasks+1))
    fi
    if [[ "${task_completed[i]}" == "$current_view" || "$current_view" == "" ]]; then
      view_task_ids+=("${task_ids[i]}")
      cmd="
        $cmd
        stack id=${task_ids[i]} horizontal horizontalAlign='space-between' verticalAlign=center
          checkbox id=status value='${task_completed[i]}' label='${task_names[i]}' data='${task_ids[i]}'
          stack horizontal gap=0
            button id=edit icon='Edit' title='Edit todo' data='${task_ids[i]}'
            button id=delete icon='Delete' title='Delete todo' data='${task_ids[i]}'
      "      
    fi
  done
  pglet_send "$cmd"
  pglet_send "set items_left value='$active_tasks item(s) left'"
}

function change_task_status() {
  IFS='|' read -r task_id task_status <<< "$1"

  # find task by task id
  for (( i = 0; i < ${#task_ids[@]}; ++i )); do
    if [[ "${task_ids[i]}" == "$task_id" ]]; then
      task_completed[$i]="$task_status"
      update_tasks_view
      return
    fi
  done
}

function add_new_task() {
  # get task from textbox
  task=`pglet_send "get new_task value"`
  if [[ "$task" == "" ]]; then
    return
  fi

  # clear textbox
  pglet_send "set new_task value=''"

  # add task to array
  task_ids+=("$next_task_id")
  task_completed+=('false')
  task_names+=("$task")
  ((next_task_id=$next_task_id+1))

  update_tasks_view
}

function delete_task() {
  # $1 - task_id to delete

  new_task_ids=()
  new_task_completed=()
  new_task_names=()

  # find index by task id
  for (( i = 0; i < ${#task_ids[@]}; ++i )); do
    if [[ "${task_ids[i]}" != "$1" ]]; then
      new_task_ids+=("${task_ids[i]}")
      new_task_completed+=("${task_completed[i]}")
      new_task_names+=("${task_names[i]}")
    fi
  done

  task_ids=("${new_task_ids[@]}")
  task_completed=("${new_task_completed[@]}")
  task_names=("${new_task_names[@]}")

  update_tasks_view
}

function clear_completed() {
  new_task_ids=()
  new_task_completed=()
  new_task_names=()

  # find index by task id
  for (( i = 0; i < ${#task_ids[@]}; ++i )); do
    if [[ "${task_completed[i]}" != "true" ]]; then
      new_task_ids+=("${task_ids[i]}")
      new_task_completed+=("${task_completed[i]}")
      new_task_names+=("${task_names[i]}")
    fi
  done

  task_ids=("${new_task_ids[@]}")
  task_completed=("${new_task_completed[@]}")
  task_names=("${new_task_names[@]}")

  update_tasks_view
}

function edit_task() {
  # $1 - task_id to edit

  # find index by task id
  for (( i = 0; i < ${#view_task_ids[@]}; ++i )); do
    if [[ "${view_task_ids[i]}" == "$1" ]]; then
      pos="$i"
    fi
  done

  task_name=`pglet_send "get tasks:$1:status label"`

  pglet_send "replace to=tasks at=$pos
    stack id=$1 horizontal
      textbox id=edit_task value='$task_name' width='100%'
      button id=save text=Save data='$1'
  "
}

function update_task() {
  # $1 - task_id to edit
  task_name=`pglet_send "get tasks:$1:edit_task value"`
  if [[ "$task_name" == "" ]]; then
    pglet_send "set tasks:$1:edit_task errorMessage='Task cannot be blank'"
    return
  fi

  # find index by task id
  for (( i = 0; i < ${#task_ids[@]}; ++i )); do
    if [[ "${task_ids[i]}" == "$1" ]]; then
      task_names[$i]="$task_name"
      update_tasks_view
      return
    fi
  done
}

function main() {
  pglet_send "set page title='Bash TODO with Pglet' horizontalAlign='center'"
  pglet_send "add
    stack width='70%'
      text value='Todos' size=xLarge align=center
      stack horizontal
        textbox id=new_task placeholder='What needs to be done?' width='100%'
        button primary id=add text=Add
      stack gap=25
        tabs id=view
          tab key='' text='all'
          tab key='false' text='active'
          tab key='true' text='completed'
        stack id=tasks
        stack horizontal horizontalAlign='space-between' verticalAlign=center
          text id=items_left value='0 items left'
          button id=clear_completed text='Clear completed'
  "

  while true
  do
    pglet_wait_event
    echo "Event: $PGLET_EVENT_TARGET $PGLET_EVENT_NAME $PGLET_EVENT_DATA"
    control_id="$PGLET_EVENT_TARGET"
    data="$PGLET_EVENT_DATA"

    if [[ "$control_id" == "add" ]]; then
      add_new_task
    elif [[ "$control_id" == "view" ]]; then
      view="$data"
      if [[ "$view" != "$current_view" ]]; then
        current_view="$view"
        update_tasks_view
      fi      
    elif [[ "$control_id" == *:status ]]; then
      change_task_status "$data"
    elif [[ "$control_id" == *:edit ]]; then
      edit_task "$data"
    elif [[ "$control_id" == *:save ]]; then
      update_task "$data"      
    elif [[ "$control_id" == *:delete ]]; then
      delete_task "$data"
    elif [[ "$control_id" == "clear_completed" ]]; then
      clear_completed
    fi
  done
}

pglet_app "index" "main"