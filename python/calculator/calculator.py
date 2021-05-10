import pglet
from pglet import Textbox, Button, Text, Stack, Message

class CalcApp():
    #initiation
    operand1 = '0' #previous value
    operator = '+'
    start_new = True #will start new sequence in the 'result' textbox
    new_history = True #will start history from scratch
    new_dot = True #will be used to make sure no number has more than one dot

    def __init__(self):
        self.message = Message(dismiss=True, visible=False)
        self.result = Textbox(value = '0', align = 'right')
        self.history = Text()
        self.view = Stack(controls = [
            self.message,
            Stack(horizontal=True,controls=[
                self.result]),
            Stack(horizontal=True,controls=[
                Button(text='7', on_click=self.on_click, data='7'),
                Button(text='8', on_click=self.on_click, data='8'),
                Button(text='9', on_click=self.on_click, data='9'),
                Button(text='/', on_click=self.on_click, data='/')
            ]),
            Stack(horizontal=True,controls=[
                Button(text='4', on_click=self.on_click, data='4'),
                Button(text='5', on_click=self.on_click, data='5'),
                Button(text='6', on_click=self.on_click, data='6'),
                Button(text='*', on_click=self.on_click, data='*')
            ]),
            Stack(horizontal=True,controls=[
                Button(text='1', on_click=self.on_click, data='1'),
                Button(text='2', on_click=self.on_click, data='2'),
                Button(text='3', on_click=self.on_click, data='3'),
                Button(text='-', on_click=self.on_click, data='-')
            ]),
            Stack(horizontal=True,controls=[
                Button(text='0', on_click=self.on_click, data='0'),
                Button(text='.', on_click=self.on_click, data='.'),
                Button(text='=', on_click=self.on_click, data='='),
                Button(text='+', on_click=self.on_click, data='+')
            ]),
            Stack(horizontal=True,controls=[
                Button(text='C', on_click=self.on_click, data='C')
            ]),
            Stack(horizontal=True,controls=[
                Text('History: ', ), self.history
            ])
        ])

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, x, y, action):
        x_float = float(x)
        y_float = float(y)
        if action == '+':
            return self.format_number(x_float + y_float)
        elif action == '-':
            return self.format_number(x_float - y_float)
        elif action == '*':
            return self.format_number(x_float * y_float)
        elif action == '/':
            return self.format_number(x_float / y_float)
    

    def update_history(self, data):
        if self.new_history:
            if data in ('+', '-', '*', '/'):
                self.history.value = str(self.operand1) + data
            else:
                self.history.value = data
            self.new_history = False
        else:
            if data == '*' or data =='/':
                self.history.value = '(' + self.history.value + ')'
                self.history.value += data
            else:
                self.history.value += data

    def on_click(self, e):
        if e.data in ('1','2','3','4','5','6','7','8','9','0'):
                #start a new sequence in the 'result' textbox
                if self.start_new:
                    self.result.value = e.data
                    self.start_new = False
                
                #continue exising sequence in the 'result' textbox
                else:
                    self.result.value = self.result.value + e.data
                
                #update history
                self.update_history(e.data)

        if e.data == '.':
                #start a new sequence in the 'result' textbox
                if self.start_new:
                    self.result.value = '0' + e.data
                    self.start_new = False
                    self.new_dot = False
                    self.update_history(self.result.value)
                
                #continue exising sequence in the 'result' textbox
                else:
                    if self.new_dot:
                        self.result.value = self.result.value + e.data
                        self.update_history(e.data)
                        self.new_dot = False    

        elif e.data == 'C':
                self.result.value = '0'
                self.operand1 = '0'
                self.operator = '+'
                self.start_new = True
                self.new_history = True
                self.new_dot = True
                self.update_history('')
                self.view.update()

        elif e.data in ('+','-','*','/'):
                
                #self.result.value = self.calculate(self.operand1, self.result.value, self.operator)
                try:
                    self.result.value = self.calculate(self.operand1, self.result.value, self.operator)
                except:
                    self.message.visible = True
                    self.message.value = 'Cannot complete the operation'

                self.operand1 = self.result.value
                self.operator = e.data
                self.start_new = True
                self.new_dot = True
                
                #update history
                self.update_history(e.data)

        elif e.data == '=':

                try:
                    self.result.value = self.calculate(self.operand1, self.result.value, self.operator)
                except:
                    self.message.visible = True
                    self.message.value = 'Cannot complete the operation'
                
                self.operator = '+'
                self.operand1 = '0'
                self.start_new = True
                self.new_dot = True

                #update history
                self.update_history(e.data + str(self.result.value))
                self.new_history = True

        self.view.update()

def main(page):
    page.title = "Calculator App"
    page.horizontal_align = 'center'
    page.update()
    app = CalcApp()
    page.add(app.view)

pglet.app("calc-app", target=main)