import pglet
from pglet import Message, MessageButton
with pglet.page("myapp") as page:

    page.add(
      Message(type='warning', dismiss=True, value='Warning message with buttons', buttons=[
        MessageButton(text='Yes', action='yes'),
        MessageButton(text='No', action='no')
      ]),
      Message(type='severeWarning', multiline=True, value='SevereWarning defaults to multiline. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus, purus a lobortis tristique, odio augue pharetra metus, ac placerat nunc mi nec dui. Vestibulum aliquam et nunc semper scelerisque. Curabitur vitae orci nec quam condimentum porttitor et sed lacus. Vivamus ac efficitur leo. Cras faucibus mauris libero, ac placerat erat euismod et. Donec pulvinar commodo odio sit amet faucibus. In hac habitasse platea dictumst. Duis eu ante commodo, condimentum nibh pellentesque, laoreet enim. Fusce massa lorem, ultrices eu mi a, fermentum suscipit magna. Integer porta purus pulvinar, hendrerit felis eget, condimentum mauris.', buttons=[
        MessageButton('OK'),
        MessageButton('Cancel')
      ]))