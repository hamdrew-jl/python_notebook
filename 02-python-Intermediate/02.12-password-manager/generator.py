from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string

BLUE = "#A1CCD1"
YELLOW = "#F4F2DE"
ORANGE = "#E9B384"
GREEN = "#7C9D96"
FONTS_G = ("Arial", 24, "bold", "underline")
FONTS = ("Arial", 10, "normal")

# Lists of valid password characters
password_list = []
list_upper = []
list_lower = []
list_number = []
list_symbol = []


# ----------------------------  ------------------------------- #
def get_list_of_chars():
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    global list_upper, list_lower, list_number, list_symbol

    letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ----------------------------  ------------------------------- #
class GeneratorPopup:
    global list_symbol, list_number, list_lower, list_upper

    def __init__(self):

        self.password = ""
        self.password_length = 16
        self.password_upper = 1
        self.password_lower = 1
        self.password_number = 0
        self.password_symbol = 0
        self.password_number_qty = 4
        self.password_symbol_qty = 2
        self.qty_lower = 0
        self.list_password = []
        self.remaining = 16

        # ----------------------------  ------------------------------- #

        # generator UI
        self.generator_window = Tk()
        self.generator_window.title("Password Generator")
        self.generator_window.minsize(width=160, height=440)
        self.generator_window.config(padx=20, pady=50)

        # Label
        self.generator_title = Label(text="Password Generator", fg=GREEN, font=FONTS_G, width=20)
        self.generator_title.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

        self.label_password = Label(text="Password Here", width=20, height=3, relief="sunken", bg=YELLOW,
                                    fg="black", font=("arial", 20), wraplength=300)
        self.label_password.grid(column=0, row=1, columnspan=2, padx=20, pady=10)

        self.many_num_label = Label(text="How many numbers", font=FONTS)
        self.many_num_label.grid(column=0, row=7)

        self.many_sym_label = Label(text="How many symbols", font=FONTS)
        self.many_sym_label.grid(column=0, row=8)

        # Scale
        self.scale = Scale(from_=4, to=32, orient="horizontal", length=300, activebackground=GREEN, command=self.scale)
        self.scale.config(troughcolor=YELLOW, label="Password Length")
        self.scale.grid(column=0, row=2, columnspan=2, padx=20, pady=10)

        # Create a LabelFrame
        self.frame = LabelFrame(self.generator_window, text="Select the Items", padx=80, pady=20)
        self.frame.grid(column=0, row=3, columnspan=2)

        # Checkbutton
        var_upper = IntVar()
        var_lower = IntVar()
        var_num = IntVar()
        var_symbol = IntVar()

        self.check_upper = Checkbutton(self.frame, text="Uppercase (A-Z)", variable=var_upper,
                                       onvalue=1, offvalue=0, command=self.do_it)
        self.check_lower = Checkbutton(self.frame, text="Lowercase (a-z)", variable=var_lower,
                                       onvalue=1, offvalue=0, command=self.do_it)
        self.check_num = Checkbutton(self.frame, text="Number (0-9)", variable=var_num,
                                     onvalue=1, offvalue=0, command=self.do_it)
        self.check_symbol = Checkbutton(self.frame, text="Symbol (@&$!#?)", variable=var_symbol,
                                        onvalue=1, offvalue=0, command=self.do_it)

        self.check_upper.grid(column=0, row=3, sticky=W)
        self.check_lower.grid(column=0, row=4, sticky=W)
        self.check_num.grid(column=0, row=5, sticky=W)
        self.check_symbol.grid(column=0, row=6, sticky=W)

        # Button
        self.generate_button = Button(text="GENERATE", width=20, font=("Arial", 10, "bold"), fg=YELLOW, bg=GREEN)
        self.generate_button.config(borderwidth=1, relief='solid')
        self.generate_button.grid(column=0, row=10, columnspan=2, padx=10, pady=10)

        self.accept_button = Button(text="ACCEPT & COPY", width=20, font=("Arial", 10, "bold"), fg=GREEN, bg=YELLOW)
        self.accept_button.config(borderwidth=1, relief='solid')
        self.accept_button.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

        # Spinbox
        self.spinbox_num = Spinbox(from_=0, to=10, width=6, command=self.do_it)
        self.spinbox_num.grid(column=1, row=7, padx=10, pady=10)

        self.spinbox_symbol = Spinbox(from_=0, to=4, width=6, command=self.do_it)
        self.spinbox_symbol.grid(column=1, row=8, padx=10, pady=10)

        self.generator_window.mainloop()

    def scale(self, val):
        password_length = int(val)
        self.do_it

    def do_it(self):
        """Create the password every time a widget is altered"""
        self.password = ""  # Clear out any existing password
        self.remaining = self.password_length  # Number of characters in password yet to be filled

        # Get current values of checkboxes and spinboxes
        self.password_upper = self.check_upper.get()
        self.password_lower = self.check_lower.get()
        self.password_number = self.check_num.get()
        self.password_symbol = self.check_symbol.get()
        self.password_number_qty = int(self.spinbox_num.get())
        self.password_symbol_qty = int(self.spinbox_symbol.get())

        # Restrict numbers and symbols to half the password length
        if self.password_number:
            self.spinbox_num["to"] = self.password_length // 2
        if self.password_symbol:
            self.spinbox_symbol["to"] = self.password_length // 2

        # Generate the password
        if self.password_symbol:
            for _ in range(0, self.password_symbol_qty):
                self.password += choice(list_symbol)
            self.remaining = self.password_length - len(self.password)
        if self.password_number:
            for _ in range(0, self.password_number_qty):
                self.password += choice(list_number)
            self.remaining = self.password_length - len(self.password)
        if self.password_lower and self.remaining > 0:
            if self.password_upper:
                self.qty_lower = randint(1, self.remaining)
            else:
                self.qty_lower = self.remaining
            for _ in range(1, self.qty_lower):
                self.password += choice(list_lower)
            self.remaining = self.password_length - len(self.password)
        if self.password_upper and self.remaining > 0:
            for _ in range(0, self.remaining):
                self.password = self.password + choice(list_upper)
        self.list_password = list(self.password)
        shuffle(self.list_password)
        self.password = "".join(self.list_password)
        self.label_password["text"] = self.password
    # ----------------------------  ------------------------------- #


pop = GeneratorPopup()
