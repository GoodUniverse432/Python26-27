
import turtle
import random
bob = turtle.Turtle()


def draw_stars(amount, min_size, max_size, color):
    bob.speed(0)
    bob.penup()
    bob.pencolor(color)
    bob.fillcolor(color)

    for times in range(amount):
        x = random.randint(-450, 450)
        y = random.randint(-330, 330)
        size = random.randint(min_size, max_size)

        bob.goto(x, y)
        bob.pendown()
        bob.begin_fill()
        bob.circle(size)
        bob.end_fill()
        bob.penup()

def draw_polygon(points, color, outline, amount):
    bob.penup()
    bob.goto(points[0])
    bob.pencolor(outline)
    bob.fillcolor(color)
    bob.pensize(2)
    bob.pendown()
    bob.begin_fill()

    for times in range(1, amount):
        bob.goto(points[times])

    bob.goto(points[0])
    bob.end_fill()
    bob.penup()


def draw_black_hole(size, spiral_amount, center_color):
    bob.speed(0)
    bob.penup()

    # Glowing outer rings
    colors = ["purple", "blue", "violet", "magenta"]

    for times in range(4):
        bob.goto(0, -size + times * 6)
        bob.pendown()
        bob.pensize(5)
        bob.pencolor(colors[times])
        bob.circle(size - times * 6)
        bob.penup()

    # Spiral effect
    spiral_colors = ["purple", "violet", "magenta", "cyan"]

    bob.goto(0, 0)
    bob.setheading(0)
    bob.pensize(3)
    bob.pendown()

    for times in range(spiral_amount):
        bob.pencolor(spiral_colors[times % 4])
        bob.circle(times * size / 300, 18)

    bob.penup()

    # Black hole center
    bob.goto(0, -size * 0.4)
    bob.pencolor(center_color)
    bob.fillcolor(center_color)
    bob.begin_fill()
    bob.circle(size * 0.4)
    bob.end_fill()
    bob.penup()

    # Inner glowing ring
    bob.goto(0, -size * 0.48)
    bob.pencolor("cyan")
    bob.pensize(2)
    bob.pendown()
    bob.circle(size * 0.48)
    bob.penup()


def draw_ship(x, y, size, body_color, window_color, flame_color):

    # Engine flame
    flame = [(x + 38 * size, y),
        (x + 75 * size, y + 12 * size),
        (x + 62 * size, y),
        (x + 75 * size, y - 12 * size)]

    draw_polygon(flame, flame_color, "orange", 4)

    # Top wing
    top_wing = [(x - 5 * size, y + 10 * size),
        (x + 20 * size, y + 35 * size),
        (x + 35 * size, y + 12 * size),
        (x + 25 * size, y + 8 * size)]

    draw_polygon(top_wing, "blue", "cyan", 4)

    # Bottom wing
    bottom_wing = [(x - 5 * size, y - 10 * size),
        (x + 20 * size, y - 35 * size),
        (x + 35 * size, y - 12 * size),
        (x + 25 * size, y - 8 * size)]

    draw_polygon(bottom_wing, "blue", "cyan", 4)

    # Main spaceship body
    body = [(x - 50 * size, y),
        (x - 20 * size, y + 13 * size),
        (x + 25 * size, y + 13 * size),
        (x + 45 * size, y + 7 * size),
        (x + 45 * size, y - 7 * size),
        (x + 25 * size, y - 13 * size),
        (x - 20 * size, y - 13 * size)]

    draw_polygon(body, body_color, "cyan", 7)

    # Cockpit
    bob.penup()
    bob.goto(x - 5 * size, y)
    bob.pencolor("white")
    bob.fillcolor(window_color)
    bob.pendown()
    bob.begin_fill()
    bob.circle(7 * size)
    bob.end_fill()
    bob.penup()


def draw_title(title, color):
    bob.penup()
    bob.goto(0, 300)
    bob.pencolor(color)
    bob.write(
        title,
        align="center",
        font=("Arial", 22, "bold") )
