import turtle

window=turtle.Screen()
window.title("my first game")
window.bgcolor("blue")
window.setup(width=900,height=600)
window.tracer(0)


    #sol thta
sol_tahta=turtle.Turtle()
sol_tahta.speed(0)
sol_tahta.color("red")
sol_tahta.shapesize(stretch_wid=5,stretch_len=1)
sol_tahta.shape("square")
sol_tahta.penup()
sol_tahta.goto(-420,0)

    #sag_tahta
sag_tahta=turtle.Turtle()
sag_tahta.speed(0)
sag_tahta.color("red")
sag_tahta.shapesize(stretch_wid=5,stretch_len=1)
sag_tahta.shape("square")
sag_tahta.penup()
sag_tahta.goto(420,0)

    #ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx=1
ball.dy=1

#pen
pas=0
pbs=0
pen=turtle.Turtle()
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"PlayerA:{pas} PlayerB:{pbs}",align="center",font=("Courier",24,"normal"))


    #functions
def sol_yuxari():
    y=sol_tahta.ycor()
    y+=20
    sol_tahta.sety(y)

def sol_asagi():
    y=sol_tahta.ycor()
    y-=20
    sol_tahta.sety(y)

def sag_yuxari():
    y=sag_tahta.ycor()
    y+=20
    sag_tahta.sety(y)

def sag_asagi():
    y=sag_tahta.ycor()
    y-=20
    sag_tahta.sety(y)
#keys controller
window.listen()
window.onkeypress(sol_yuxari,"e")
window.onkeypress(sol_asagi,"s")
window.onkeypress(sag_asagi,"Down")
window.onkeypress(sag_yuxari,"Up")



while True:
    window.update()


    ball.setx((ball.xcor()+ball.dx))
    ball.sety((ball.ycor()+ball.dy))

    #limit
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>440:
        pas+=1
        pen.clear()
        pen.write(f"PlayerA:{pas} PlayerB:{pbs}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1

    if ball.xcor()<-440:
        pbs+=1
        pen.clear()
        pen.write(f"PlayerA:{pas} PlayerB:{pbs}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1

    if ball.xcor()>400 and (ball.ycor()<sag_tahta.ycor()+30 and ball.ycor()>sag_tahta.ycor()-30):
        ball.dx*=-1

    if ball.xcor()<-400 and (ball.ycor()<sol_tahta.ycor()+30 and ball.ycor()>sol_tahta.ycor()-30):
        ball.dx*=-1

    if sol_tahta.ycor()>260:
        sol_tahta.sety(260)

    if sol_tahta.ycor()<-260:
        sol_tahta.sety(-260)

    if sag_tahta.ycor()>260:
        sag_tahta.sety(260)

    if sag_tahta.ycor()<-260:
        sag_tahta.sety(-260)
