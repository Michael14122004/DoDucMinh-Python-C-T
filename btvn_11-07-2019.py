from turtle import*

shape('turtle')
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)

for i in range (1):
    color(colors[i])
    for i in range(3):
        i = 0
        forward(100)
        left(120)
left(90)

for i in range (2):
    color(colors[i])
    for i in range(4):
        i = 0
        forward(100)
        right(90)
left(18)

for i in range (3):
    color(colors[i])
    for i in range(5):
        i = 0
        forward(100)
        right(72)
left(12)

for i in range (4):
    color(colors[i])
    for i in range(6):
        i = 0
        forward(100)
        right(60)
left(8.5)

for i in range (5):
    color(colors[i])
    for i in range(7):
        forward(100)
        right(360/7)

mainloop()
