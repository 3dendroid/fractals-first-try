import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.color('orange')

# l - settings
gens = 20
axiom = 'A'
chr_1, rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'
step = 50
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else rule_2 for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 + 60)
turtle.clear()
turtle.write(f'generation: {gens}', font=('Arial', 60, 'normal'))

axiom = get_result(gens, axiom)

for chr in axiom:
    if chr == chr_1:
        leo.left(60)
        leo.forward(step)
    elif chr == chr_2:
        leo.right(60)
        leo.forward(step)

screen.exitonclick()
