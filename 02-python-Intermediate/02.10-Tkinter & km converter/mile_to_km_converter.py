from tkinter import *

FONTS = ("Arial", 12)


def button_clicked():
    print("I get calculate")
    result = round(1.60934 * int(my_input.get()), 2)
    label_4["text"] = result


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)

label_1 = Label(text="is equal to", font=FONTS)
label_2 = Label(text="Miles", font=FONTS)
label_3 = Label(text="Km", font=FONTS)
label_4 = Label(text="0", font=FONTS)

label_1.grid(column=12, row=12)
label_2.grid(column=24, row=6)
label_3.grid(column=24, row=12)
label_4.grid(column=16, row=12)

my_input = Entry(width=10)
my_input.grid(column=16, row=6)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=16, row=18)

window.mainloop()
