import time
import pglet
from pglet import Text, Progress, Stack

page = pglet.page()
page.horizontal_align = 'stretch'

prog1 = Progress("Copying file1.txt to file2.txt", value=0, width='50%')

page.add(Text("Default Progress", size='xLarge'), prog1)
    
for i in range(0, 101):
    prog1.value = i
    prog1.update()
    time.sleep(0.005)

prog2 = Progress("Provisioning your account", value=0, width='50%')
page.add(prog2)

progress = [
    ("Preparing environment...", 0), 
    ("Collecting information...", 20), 
    ("Creating database entities...", 40), 
    ("Verifying the data...", 60), 
    ("Finishing the process, almost done...", 80), 
    ("Your account has been created!", 100)
]

for p in progress:
    prog2.description = p[0]
    prog2.value = p[1]
    prog2.update()
    time.sleep(2)

