import turtle

def draw_poly(tess, n, sz):
    """
    Draws a regular polygon, with number of sides equal to n and 
    size of each side equal to sz. The parameter tess is an instance of the Turtle class
    """
    screen = turtle.Screen()
    angle = 360/n
    for i in range(n):
        tess.forward(sz)
        tess.left(angle)
    screen.mainloop()

if __name__ == "__main__":
    agent = turtle.Turtle()
    agent.pencolor("pink")
    agent.pensize(3)
    draw_poly(agent, 8, 50)
