import turtle
import pandas

WIDTH, HEIGHT = 725, 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("U.S. States Quiz")
image = "Udemy/US States Quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Udemy/US States Quiz/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 States Correct", prompt="Enter a State's name.").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()