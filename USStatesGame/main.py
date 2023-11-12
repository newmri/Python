import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if state in states:
        guessed_states.append(state)
        turtle = turtle.Turtle()
        turtle.hideturtle()
        turtle.penup()
        state_data = data[data.state == state]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(state)

screen.exitonclick()