import turtle,time
sc=turtle.Screen()
pen=turtle.Turtle()

def semi_circle(col,rad,val):
    pen.color(col)
    pen.circle(rad,-100)
    pen.up()
    pen.setpos(val,0)
    pen.down()
    pen.right()
col=['violet','red','green','blue','orange','yellow','indigo']

sc.setup(800,600)
sc.bgcolor('black')

pen.right(90)
pen.width(10)
pen.speed(7)




for i in range(7):
    semi_circle(col[i],10*(i+8),-10*(i+1))
