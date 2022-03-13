Form control example
--------------------

This directory contains a example of using the Form control. The example is a "manual" app that
contains several pages, each demonstrating different aspects of using the Form control.

- `main.py` contains the code to run the manual, and can itself be considered an example of this 
  type of multi-page app. It has no other dependencies than pglet, and does not use the Form
  control.

- `manual_content.py` contains the manual pages as methods of the class Content. Method docstrings
  become the text on the page, method code is displayed under the text (by default), and the UI
  created by the running code is visible beside the text.

  If you run the manual app with this manual content, you should have these dependencies installed:
  
  - `pydantic` for the pydantic examples
  - `pydantic[email]` for the email validator in pydantic
  - `typing_extensions` if you are running Python <3.8
