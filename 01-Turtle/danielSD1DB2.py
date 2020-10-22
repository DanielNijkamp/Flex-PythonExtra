#setup turtle graphics

import turtle

turtle.setup (800, 800, 0, 0)

turtle.reset()
turtle.pencolor("Black")
turtle.speed (-100)
for x in range(360):
  turtle.circle(500)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.forward(300)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.circle(200)
  turtle.right(1)
turtle.done()
