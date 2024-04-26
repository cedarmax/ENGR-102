import turtle as t

t.color('maroon')   #  Gotta have maroon ink
t.pensize(10)       #  Sets the pen width to 10
t.up()              #  Pick up pen - no drawing

#  Drawing lettter A
t.setpos(-70,40)
t.down()            # Put pen down - start drawing A
t.setpos(-50,120)
t.setpos(-30,40)
t.up()
t.setpos(-60,80)
t.down()
t.setpos(-40,80)
t.up()              #  Pick up pen - no drawing, end of A

#  Drawing letter T
t.setpos(-30,10)
t.down()            # Put pen down - start drawing T
t.setpos(30,10)
t.up()
t.setpos(0,10)
t.down()
t.setpos(0,150)
t.up()
t.setpos(-90,120)
t.down()
t.setpos(-90,150)
t.setpos(90,150)
t.setpos(90,120)
t.up()              #  Pick up pen - no drawing, end of T

#  Drawing letter M
t.setpos(30,40)
t.down()            # Put pen down - start drawing M
t.setpos(40,120)
t.setpos(50,70)
t.setpos(60,120)
t.setpos(70,40)
t.up()              #  Pick up pen - no drawing, end of M

t.done()            #  Stops the turtle
input()             #  So that the window doesn't disappear