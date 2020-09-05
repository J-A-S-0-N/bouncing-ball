import turtle

speed = 0
color = "red"
shape = "circle"


def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("bouncing ball")
    
    ball = turtle.Turtle(shape)
    ball.color(color)
    ball.penup()
    ball.speed(speed)
    ball.goto(0,200)
    ball.dy = -2
    gravity = 0.1
    
    while True:

        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() < -400:
            ball.dy *= -1 


    wn.mainloop()
    

if __name__ == "__main__":
    main()