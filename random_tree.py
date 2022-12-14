import turtle
from random import randint

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)
screen.bgpic('src/photos/wp.gif')  # for adding background

# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.penup()
leo.setpos(0, -HEIGHT // 5 - 25)  # coord of the tree
leo.pendown()
leo.color('black')  # color

# l-system settings
gens = 9  # gens, 9 is optimal
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 60  # size of the tree
angle = lambda: randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))

axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
for chr in axiom:
    leo.color(color)
    if chr == 'F' or chr == 'X':
        leo.forward(step)
    elif chr == '@':
        step -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif chr == '+':
        leo.right(angle())
    elif chr == '-':
        leo.left(angle())
    elif chr == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
    elif chr == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

axiom = apply_rules(axiom)

screen.exitonclick()
