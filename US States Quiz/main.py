import turtle
import pandas

#Width and height of the screen in pixels.
WIDTH, HEIGHT = 725, 500

#Setup the screen.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("U.S. States Quiz")
image = "Udemy/US States Quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Read state data and create a list of all states.
data = pandas.read_csv("Udemy/US States Quiz/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

#Run the game until all 50 states are guessed correctly.
while len(guessed_states) < 50:
    
    #Prompt the user to answer a state.
    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 States Correct", prompt="Enter a State's name.").title()

    #End the game if user types 'exit'.
    if answer_state == "Exit":
        
        #Create a list of the missed states.
        missing_states = [state for state in all_states if state not in guessed_states]

        #Convert the list of missing states to a csv file.
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #If answer is correct, add it to the guessed_states list and display it on the screen at the given position.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())