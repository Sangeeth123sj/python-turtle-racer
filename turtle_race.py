import turtle
import time
import random
WIDTH, HEIGHT = 1000, 1000
COLORS = ['red','blue','green','cyan','brown','yellow','orange']
def get_no_of_racers():
    racers = 0
    while True:
        racers = input("Enter number of turtles: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input not numeric! try again")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Input not between 2 and 10! try again")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle racer!")

def create_turtles(colors,spacer):
    turtles = []
    spaceradd = spacer
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('circle')
        racer.color(color)
        racer.penup()
        racer.left(90)
        racer.setpos(-(WIDTH/2)+spaceradd,-(HEIGHT/2) + 50)
        racer.pendown()
        spaceradd = spaceradd + spacer
        turtles.append(racer)
    return turtles

def race_turtles(colors, turtles):
    while True:
        for turtle in turtles:
            print(turtle)
            jump = random.randrange(2,9)
            turtle.forward(jump)
            x,y =  turtle.pos()
            if y > (HEIGHT/2-20):
                winner_color = colors[turtles.index(turtle)]
                print(winner_color+" has won!")
                return
            
racers = get_no_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
spacer = int(WIDTH/(racers+1))
turtles = create_turtles(colors,spacer)
race_turtles(colors,turtles)
#time.sleep(10)
