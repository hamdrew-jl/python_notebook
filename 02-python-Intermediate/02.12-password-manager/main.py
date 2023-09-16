from tkinter import *
from tkinter import messagebox
import random
import pyperclip


FONTS = ("Arial", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '&', '$', '!', '#', '?']

    password_list = []

    password_letter = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    if passw_entry.index("end") == 0:
        passw_entry.insert("0", password)
        pyperclip.copy(password)
    else:
        passw_entry.delete("0", "end")
        passw_entry.insert("0", password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if web_entry.index("end") == 0 or passw_entry.index("end") == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=f"{web_entry.get()}",
                                       message=f"These are the details entered: \n\nEmail: {email_entry.get()}"
                                               f"\nPassword: {passw_entry.get()} \n Is it ok to save?")
        if is_ok:
            with open("my_password.txt", "a") as f:
                information = f"{web_entry.get()} | {email_entry.get()} | {passw_entry.get()}\n"

                web_entry.delete(0, "end")
                email_entry.delete(0, "end")
                email_entry.insert(0, "xxxx@gmail.com")
                passw_entry.delete(0, "end")

                f.write(information)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label
web_label = Label(text="Website:", font=FONTS)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=FONTS)
email_label.grid(column=0, row=2)

passw_label = Label(text="Password:", font=FONTS)
passw_label.grid(column=0, row=3)

# Button
gener_button = Button(text="Generate Password", font=FONTS, command=generate_password)
gener_button.grid(column=2, row=3)

add_button = Button(text="Add", font=FONTS, width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Entry
web_entry = Entry(width=46)
web_entry.grid(column=1, row=1, columnspan=2)
# focus()
web_entry.focus()

email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2)

# insert()
email_entry.insert(END, "xxxx@gmail.com")

passw_entry = Entry(width=28)
passw_entry.grid(column=1, row=3)

window.mainloop()
