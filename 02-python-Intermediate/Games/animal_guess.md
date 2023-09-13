# Animal Guessing Game

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/5bcae0c5-af64-44ec-a2e4-428d9532cfe8)



## 1. Make the background pic
* Prepared in Photoshop or Powerpoint

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/968651f1-c7e0-4afa-8e39-fe5a29cc486c)


## 2. Grab coor data from the image
### 2.1 Get mouse click coordinates in Python turtle 
```python
import turtle

screen = turtle.Screen()
image_main = "./image/main_animal.gif"
screen.setup(width=700, height=394)
screen.addshape(image_main)
turtle.shape(image_main)

def get_mouse_click_coor(x, y):
    """Get mouse click coordinates in Python turtle"""
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
```
### 2.2 Make a Excel file and sort it
* Check the mistake
* Save as .csv file

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/dc2f1bf9-5e5f-4ba1-83f2-6b2f6c015507)


* File preparation
1. main.py
2. animal_guess.csv
3. grab_coor.py
4. image(cover and main background picture)


## 3.Steps
### 3.1 Import and set screen
```python
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
```
### 3.2 Pandas data
```python
data = pandas.read_csv("animal_guess.csv")
all_animals = data["name"].to_list()  # DO NOT FORGET ()
```
### 3.3 Main loop

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/52b13fcc-7db5-4c89-87c1-0cc3242bd26a)


```python
guess_animals = []
score = 0

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
```
### 3.4 Adjustment
* when test the game, change the word's location slightly to ensure each word on animal image perfectly.
```python
ADJUST_X = -10
ADJUST_Y = -10

```
* Add guessed word on the list 

![image](https://github.com/hamdrew-jl/python_notebook/assets/141601957/3d3a24da-e0ce-4a6d-b0b1-a4af23ad355c)


```python
y_word = [47, 41, 35, 29, 23, 17, 11, 5, -1, -7, -13, -19, -25, -31, -37, -43, -49, -55, -61, -67, -73,
          -79, -85, -91, -97, -103, -109, -115, -121, -127, -133, -139, -145]
```


#### TODO
1. time calculation
2. score result showing on the screen
