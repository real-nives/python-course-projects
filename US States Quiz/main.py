import turtle

WIDTH, HEIGHT = 725, 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("U.S. States Quiz")
image = "Udemy/US States Quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="Enter a State's name.")

screen.exitonclick()