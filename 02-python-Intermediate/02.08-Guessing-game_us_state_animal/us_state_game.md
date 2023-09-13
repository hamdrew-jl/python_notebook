# U.S. States Guess Game 

## Set the screen
### Add Image.
* Add a turtle shape to TurtleScreen’s shapelist.
* Only thusly registered shapes can be used by issuing the command shape(shapename).
```python
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")

# Add Image.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
```

## Get mouse click coordinates in Python turtle
* The coordinate have shown in the 50_states.csv file
```python
def get_mouse_click_coor(x, y):
    """Get mouse click coordinates in Python turtle"""
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()  # keeping screen open when the code has finished running
```

## Challenge
1. convert the guess to Title case
2. check if the guess is among the 50 states
3. write correct guesses onto the map
4. use a loop to allow the user to keep guessing
5. record the correct guesses in a list
6. keep track of the score

### Create a file to restore the data 
* if player exit the game
```python
# create states_to_learn.csv
missing_states = []
for state in state_list:
    if state not in already_guessed:
        missing_states.append(state)
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
```
### Tutorial

```python
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
data = pandas.read_csv("us state guess game/50_states.csv")
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

```
Note: After learning list comprehension, change some code above.
```python
missing_states = []
for state in state_list:
     if state not in already_guessed:
         missing_states.append(state)
```
* Change into
```python
missing_states = [state for state in state_list if state not in already_guessed]
```

### Full Code (Self Write)

```python
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
data = pandas.read_csv("us state guess game/50_states.csv")
state_list = data["state"].to_list()

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

```
### Think 
* pandas: row extract from data
* be aware: When scratch from data.  title(), lower() 
* be aware: integer and string.  int()
* add 'special keyword' to exit the program, use 'break'
* create a file to save the data
* learn how to list the missing data
* add bgpic in turtle
* TODO add counting time?
