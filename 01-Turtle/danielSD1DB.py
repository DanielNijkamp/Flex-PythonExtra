#setup turtle graphics

import turtle

turtle.setup (800, 800, 0, 0)

turtle.reset()
turtle.pencolor("Black")
turtle.speed (-40)
for x in range(500):
  turtle.forward(600)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.forward(600)
  turtle.right(90)
  turtle.right(1)
turtle.done()
