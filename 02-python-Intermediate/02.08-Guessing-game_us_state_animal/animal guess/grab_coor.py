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

