import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Arial", 10, "normal")
guess_num = 0
is_go_on = True
already_guessed = []

screen = Screen()
screen.title("U.S. States Game")

# Add Image.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# writer
writer = turtle.Turtle()
writer.hideturtle()

# pandas data
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()  # state_list = data.state.to_list()


while is_go_on:
    answer_state = screen.textinput(title=f"{guess_num}/{len(state_list)}  State Correct",
                                    prompt="What's another state's name?").title()

    for states in state_list:
        if answer_state == states:
            guess_num += 1
            current_row = data[data.state == answer_state]
            # x_cor = int(current_row["x"])
            # y_cor = int(current_row["y"])
            x_cor = int(current_row.x)
            y_cor = int(current_row.y)
            already_guessed.append(answer_state)

            writer.penup()
            writer.goto(x_cor, y_cor)
            writer.write(answer_state, font=FONT)

turtle.mainloop()




