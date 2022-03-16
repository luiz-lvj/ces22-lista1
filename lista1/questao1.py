import turtle

def draw_square(size, agent):
    """
    Draws a square which has the side equals to the size parameter and is drawn by the agent,
    which is an instance of the class Turtle
    """
    agent.forward(size)
    agent.left(90)
    agent.forward(size)
    agent.left(90)
    agent.forward(size)
    agent.left(90)
    agent.forward(size)

def move_next_position(dist, agent):
    """
    Moves the position of the pen (parameter agent) to the position where the next square will be drwn.
    """
    agent.penup()
    agent.right(90)
    agent.forward(dist)
    agent.left(90)
    agent.forward(dist)
    agent.left(90)
    agent.pendown()

def draw_picture_squares(initial_size, increment, number_squares):
    """
    Creates the picture with multiple squares, based on the number of squares, the side of the smallest 
    (and innermost) ad the increment to the squares in the outside
    """
    screen = turtle.Screen()
    agent = turtle.Turtle()
    agent.pencolor("pink")
    agent.pensize(3)
    square_size = initial_size
    for i in range(number_squares-1):
        draw_square(square_size, agent)
        move_next_position(increment/2, agent)
        square_size += increment
    draw_square(square_size, agent)
    screen.mainloop()

if __name__ == "__main__":
    draw_picture_squares(20, 20, 5)
