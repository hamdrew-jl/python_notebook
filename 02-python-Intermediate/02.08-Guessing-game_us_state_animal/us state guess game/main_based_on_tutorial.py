import turtle
import pandas

FONT = ("Arial", 10, "normal")
is_go_on = True
already_guessed = []

screen = turtle.Screen()
screen.title("U.S. States Game")

# Add Image.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# pandas data
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()  # state_list = data.state.to_list()

score = 0
while len(already_guessed) < 50:
    answer_state = screen.textinput(title=f"{score}/{len(state_list)}  State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":

        # create states_to_learn.csv
        missing_states = []
        for state in state_list:
            if state not in already_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in state_list:
        already_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # or t.write(state_data.state.item())
        score += 1






