#setup turtle graphics

import turtle

turtle.setup (800, 800, 0, 0)

turtle.reset()
turtle.pencolor("Black")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.speed (-100)
for x in range(360):
  turtle.right(1)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.right(3)
turtle.end_fill()
