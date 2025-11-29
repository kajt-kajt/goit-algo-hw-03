import turtle
import sys

def koch_side(t: turtle.Turtle, degree: int, distance: int):
    """
    Drawing one side of Koch curve
    """
    if degree == 0:
        t.forward(distance)
    else:
        for angle in [60, -120, 60, 0]:
            koch_side(t, degree-1, distance // 3)
            t.left(angle)

def koch_snowflake(t: turtle.Turtle, degree: int, side: int):
    """
    Drawing snowflake consisting of 3 curves
    """
    koch_side(t, degree, side)
    t.right(120)
    koch_side(t, degree, side)
    t.right(120)
    koch_side(t, degree, side)

def main():
    """
    Entry point
    """
    # Parameter can be passed either as a command line argument, or as a direct input by user.
    # Let's ensure it is an integer with non-negative value
    fractal_iteration = None
    if len(sys.argv)==2:
        try:
            fractal_iteration = int(sys.argv[1])
            if fractal_iteration < 0:
                fractal_iteration = None
        except ValueError:
            pass
    while fractal_iteration is None:
        # let's ask user for input till the correct value is provided
        try:
            fractal_iteration = int(input("Enter Koch snowflake iterations (number between 0 and 5 is advised): "))
            if fractal_iteration < 0:
                fractal_iteration = None
        except ValueError:
            pass
    try:
        # set screen coordinates and size
        screen = turtle.Screen()
        screen_width = 600
        screen_height = 700
        screen.setup(width=screen_width, height=screen_height)
        screen.setworldcoordinates(0, 0, screen_width, screen_height)
        # initial turtle positioning
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(50, screen_height-200)
        t.pendown()
        # speedup animation
        t.speed(10)

        # draw snowflake
        koch_snowflake(t, fractal_iteration, 500)
        
        screen.mainloop()
    except turtle.Terminator:
        # ignoring exception when closing the window
        pass


if __name__ == "__main__":
    main()
