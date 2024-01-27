from turtle import Turtle, Screen
from tkinter import Radiobutton, IntVar, Button

t = Turtle()
color_value = IntVar()  # global variable to store colour value from radio buttons
s = Screen()


def draw_feather(r, angle, color):
    """
    This function draws one feather. This function takes r-radius, angle and color as parameters.
    Drawing a feather half circle is drawn then immediately turtle shifts left and draws next half circle
    in reverse direction. Fill the colour while drawing.
    Example:
        draw_feather(100,90,"Red"):
            - This will draw feather with radius=100, angle of circle=90 and colour is Red
    """
    t.fillcolor(color)
    for i in range(2):
        t.begin_fill()
        t.circle(r, angle)
        t.left(180 - angle)
        t.end_fill()


def draw_feathers(n=3, c="white"):
    """
    This function takes number of feathers <n> and color <c> as parameters. Then draws each feather with the
    help of <draw_feather>(...) function. Default 3 and white coloured feathers will be drawn.

        Example1:
        draw_feathers()
            - This will draw 3-feathers and white coloured, which are default values.


        Example2:
        draw_feathers(5)
            - This will draw 5-feathers(user given value) and white coloured(default).

        Example3:
        draw_feathers(7,"Red")
            - This will draw 7-feathers and red coloured, which are user parameter values.
    """
    radius = 100
    angle = 90
    for i in range(n, 0, -1):
        draw_feather(radius, angle, c)
        t.left(15)


def draw_body(draw_color="black", fill_color="grey", size=3):
    """
    This function draws the body(simple circle) with border color(black-default), grey-fill colour and pen size=3.

        Example1:
        draw_body()
            - This will draw black bordered body(circle), filled with grey and pen size is 3(default values)

        Example2:
        draw_body("Green","Red")
            - This will draw Green bordered body(circle), filled with Red and pen size is 3(default)

        Example3:
        draw_body("Yellow","Blue",size=1)
            - This will draw Yellow bordered body(circle), filled with Blue and pen size is 2. All parameters
            are user given values.
    """
    t.pen(pencolor=draw_color, fillcolor=fill_color, pensize=size, speed=9)
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def draw_head(draw_color="black", fill_color="cyan", size=3):
    """
    This function draws the head(simple circle) with border color(black-default), cyan-fill colour and pen size=3.
        Example:
        draw_head(draw_color="Cyan", fill_color="Blue)
            - This will draw Cyan bordered head(circle), filled with Blue and pen size is 3(default).
    """
    t.pen(pencolor=draw_color, fillcolor=fill_color, pensize=size, speed=9)
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def draw_eyes():
    """
    This function draws the two eyes(left/right) with black-fill colour and pen size=1.
        Example:
        draw_eyes()
            - This will draw both left and right eyes with radius of 3 and always colour in black
    """
    # left
    t.up()
    t.goto(0, 30)
    t.down()
    t.pen(fillcolor="black", pensize=1, speed=9)
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # right
    t.up()
    t.goto(10, 30)
    t.down()
    t.pen(fillcolor="black", pensize=1, speed=9)
    t.begin_fill()
    t.circle(3)
    t.end_fill()


def draw_legs():
    """
    This function draws the two legs(left/right-lines) with black-fill colour and pen size=5.

        Example:
        draw_legs()
            - This will draw both left and right legs black.
    """

    # left leg
    t.up()
    t.goto(10, -40)
    t.down()
    t.pen(fillcolor="black", pensize=5, speed=9)
    t.backward(40)
    t.right(90)
    t.forward(10)

    # right leg
    t.up()
    t.goto(0, -40)
    t.left(80)
    t.down()
    t.pen(fillcolor="black", pensize=5, speed=9)
    t.backward(40)
    t.left(90)
    t.forward(10)


def get_value():
    """
    This function helps to drawing bird. Converts three colour values to named constants(0-Red, 1-Green,2-Blue)
    and returns the colour name. It is helper function to draw_bird()
        Example:
            get_value()
                - Returns string constant name for the integers 0/1/2.
    """
    color_names = ["Red", "Green", "Blue"]
    col_name = color_names[color_value.get()]
    return col_name


def draw_bird():
    """
    This function calls other functional components(draws feathers,body,head,eyes and legs) of the turkey-bird.
    It is invoked by event command of any GUI components like button click.
        Example:
            draw_bird()
                - It draws all turkey bird components by calling inside functions
    """
    t.clear()
    t.reset()
    col_name = get_value()
    draw_feathers(7, col_name)
    t.up()
    t.goto(30, 0)  # x-column, y-row
    t.down()
    draw_body()
    t.up()
    t.goto(20, 30)
    t.down()
    draw_head()
    draw_eyes()
    draw_legs()


def put_controls():
    """
    This function launch all initial components(Radio buttons for colours) on the screen canvas. And drawing the bird
    is initiated by Button control
        Example:
            put_controls()
                - Gets the canvas from the screen and launches 3 colors radio button and 1 draw button, which
                  starts drawing with selected colour. This is driver/controller function to the entire project.
    """
    canvas = s.getcanvas()
    c1 = Radiobutton(canvas.master, text="RED", value=0, variable=color_value)
    c2 = Radiobutton(canvas.master, text="GREEN", value=1, variable=color_value)
    c3 = Radiobutton(canvas.master, text="BLUE", value=2, variable=color_value)
    c1.pack()
    c1.place(x=30, y=30)
    c2.pack()
    c2.place(x=80, y=30)
    c3.pack()
    c3.place(x=150, y=30)
    button = Button(canvas.master, text="Draw", command=draw_bird)
    button.pack()
    button.place(x=230, y=30)


put_controls()
s.mainloop()
