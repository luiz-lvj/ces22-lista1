import turtle

size_agent = 3

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

def draw_picture_squares(initial_size, increment):

    """
    Creates the picture with multiple squares, based on the number of squares, the side of the smallest 
    (and innermost) ad the increment to the squares in the outside
    """
    square_size = initial_size
    while True:
        screen.onkey(agent_color_red, 'r')
        screen.onkey(agent_color_red, "R")

        screen.onkey(agent_color_green, 'g')
        screen.onkey(agent_color_green, "G")

        screen.onkey(agent_color_blue, 'b')
        screen.onkey(agent_color_blue, "B")

        screen.onkey(agent_size_plus, '+')
        screen.onkey(agent_size_minus, '-')

        #Apagar tudo que a turtle fez quando apertar espaço 
        screen.onkey(clear_turtle, "space")

        #Muda a posicao da turtle e continua
        screen.onkey(backward_turtle, "l")

        turtle.listen()
        draw_square(square_size, agent)
        move_next_position(increment/2, agent)
        square_size += increment


def clear_turtle():
    agent.clear()

def backward_turtle():
    agent.left(90)
    agent.forward(1)

def agent_color_red():
    agent.pencolor("red")
def agent_color_green():
    agent.pencolor("green")

def agent_color_blue():
    agent.pencolor("blue")

def agent_size_plus():
    global size_agent
    if size_agent >=20 or size_agent <= 1:
        return
    size_agent = size_agent + 1
    agent.pensize(size_agent)
    print(size_agent)

def agent_size_minus():
    global size_agent
    if size_agent >=20 or size_agent <= 1:
        return
    size_agent = size_agent - 1
    agent.pensize(size_agent)
    print(size_agent)


if __name__ == "__main__":
    global agent, screen
    screen = turtle.Screen()
    agent = turtle.Turtle()
    agent.pencolor("pink")
    agent.pensize(3)
    draw_picture_squares(40,40)