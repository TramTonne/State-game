import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states)<50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 State Correct", 
                                    prompt="What's a state's name?").title() #make the first character capitalized
    print(answer_state)

    #if the answer is one of the states
    #Then write the correct state onto the image where the x,y-cor of that state
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
screen.exitonclick(state_data.state)