import turtle

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.
border = turtle.clone()
turtle.hideturtle()
turtle.goto(-50,-50)
turtle.pendown()
turtle.goto(-50, 50)
turtle.goto(50,50)
turtle.goto(50,-50)
