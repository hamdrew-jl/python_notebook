import turtle
import time
import pandas


screen = turtle.Screen()
image_cover = "./image/cover_animal.gif"
image_main = "./image/main_animal.gif"
screen.setup(width=700, height=400)
screen.title("Guess Who I Am!")

screen.addshape(image_cover)
turtle.shape(image_cover)
time.sleep(1.2)
screen.clear()
screen.addshape(image_main)
turtle.shape(image_main)

data = pandas.read_csv("animal_guess.csv")
all_animals = data["name"].to_list()  # DO NOT FORGET ()
guess_animals = []
score = 0
ADJUST_X = -10
ADJUST_Y = -10
y_word = [47, 41, 35, 29, 23, 17, 11, 5, -1, -7, -13, -19, -25, -31, -37, -43, -49, -55, -61, -67, -73,
          -79, -85, -91, -97, -103, -109, -115, -121, -127, -133, -139, -145]

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
is_go_on = True

while is_go_on:
    if len(guess_animals) < len(all_animals):
        # popup
        answer_animals = screen.textinput(title=f"{score}/{len(all_animals)} animals guessed.",
                                          prompt="Guess an animal: ").lower()

        if answer_animals == "exit":
            miss_animal = []
            for miss in all_animals:
                if miss not in guess_animals:
                    miss_animal.append(miss)
            new_data = pandas.DataFrame(miss_animal)
            new_data.to_csv("animal_need_to_learn.csv")
            break

        if (answer_animals in all_animals) and (answer_animals not in guess_animals):
            guess_animals.append(answer_animals)
            score += 1

            current_animal_row = data[data.name == answer_animals]
            writer.goto(int(current_animal_row.x) + ADJUST_X, int(current_animal_row.y) + ADJUST_Y)
            writer.color("lime")
            writer.write(answer_animals, font=("Arial", 12, "bold"))

            writer.goto(225, y_word[score])
            writer.color("black")
            writer.write(f"{score}: {answer_animals}", font=("Arial", 6, "bold"))

    else:
        writer.goto(0, 0)
        writer.color("black")
        writer.write(f"Good Job", font=("Arial", 40, "bold"))






