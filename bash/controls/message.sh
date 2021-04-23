# include Pglet helper
source <(curl -s https://pglet.io/pglet.sh)

function main() {
  pglet_send "set page horizontalAlign='stretch'"
  pglet_send "add
  message value='This is just a message.'
  message type=success value='All files have been successfully copied.' dismiss
  message type=error value='User with specified email was not found.' dismiss
  message type=blocked truncated value='Blocked MessageBar - single line, with dismiss button and truncated text. Truncation is not available if you use action buttons or multiline and should be used sparingly. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris. You\'ve been warned!' dismiss
  message type=warning dismiss value='Watch out! You\'ve been warned!'
    button text=Yes action=yes
    button text=No action=no
  message type=warning multiline value='Warning defaults to multiline. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris.'
    button text=OK
    button text=Cancel  
  "
}

pglet_app "index" "main"