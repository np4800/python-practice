import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_fd():
    tim.forward(10)

def move_rt():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    

def move_lt():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_bk():
    tim.backward(10)

def draw_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(fun=move_fd,key="w")
screen.onkey(fun=move_rt,key="d")
screen.onkey(fun=move_lt,key="a")
screen.onkey(fun=move_bk,key="s")
screen.onkey(fun=draw_clear,key="c")

screen.exitonclick()