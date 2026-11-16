from myFunctions2 import*

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Journey Into The Unknown")
screen.setup(1000, 750)
turtle.colormode(255)

bob.speed(0)
bob.hideturtle()

# STAR SETTINGS
draw_stars(120,2,5,"white")
  

# BLACK HOLE SETTINGS
draw_black_hole(100,180,"black")

# SPACESHIP SETTINGS
draw_ship(280,40,1,"light blue","cyan","orange")

# TITLE SETTINGS
draw_title()

screen.mainloop()
