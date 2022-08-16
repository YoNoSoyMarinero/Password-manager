from tkinter import IntVar, StringVar, Tk
from Password import Password
import ttkbootstrap as ttk
from ttkbootstrap import dialogs
from ttkbootstrap.constants import *
from pyperclip import copy
from ShowPass import ShowPasswords


class App():
    def regime_validation(self):
        if (self.__digits_.get() == 0 and self.__uppercase_.get() == 0 and self.__lowercase_.get() == 0 and self.__symbols_.get() == 0):
            dialogs.Messagebox.ok(
                "Please select at least one checkbutton!", title="Warning!", alert=True)
            return False
        else:
            return True

    def input_validation(self):
        try:
            if (int(self.__pass_len.get()) < 2):
                dialogs.Messagebox.ok(
                    "Your input was incorrect!\nPassword length must be greater then 5!\nUsername has to to be 2 letters long!\nCheck if your adress is long enough!", title="Warning!", alert=True)
                return False
        except ValueError:
            dialogs.Messagebox.ok(
                "Your input was incorrect!\nPassword length must be greater then 5!\nUsername has to to be 2 letters long!\nCheck if your adress is long enough!", title="Warning!", alert=True)
            return False
        if (len(self.__username.get()) < 1 or len(self.__website.get()) < 2):
            dialogs.Messagebox.ok(
                "Your input was incorrect!\nPassword length must be greater then 5!\nUsername has to to be 2 letters long!\nCheck if your adress is long enough!", title="Warning!", alert=True)
            return False
        return True

    def generate_password(self):

        if not self.input_validation():
            return
        if not self.regime_validation():
            return
        self.__passsword = Password(self.__website.get(),
                                    self.__username.get(), int(self.__pass_len.get()), self.__digits_.get() == 1, self.__uppercase_.get() == 1, self.__lowercase_.get() == 1, self.__symbols_.get() == 1)

        self.__passsword.generate_password()
        self.__password_str.set(self.__passsword.password)
        self.__is_generated = True

    def restart_after_save(self):
        self.__pass_len.set("")
        self.__password_str.set("")
        self.__username.set("")
        self.__website.set("")
        self.__is_generated = False
        self.__passsword = None

    def save_password(self):
        if not self.__is_generated:
            dialogs.Messagebox.ok(
                "Please, generate your password first!", title="Warning!", alert=True)
            return
        self.__passsword.save_password()
        dialogs.Messagebox.ok(
            "You successfully saved your password, click show to see them all!", title="Notification!", alert=True)

        self.restart_after_save()

    def copy_to_clipboard(self):
        copy(self.__password_str.get())

    def show_passwords(self):
        ShowPasswords()

    def __init__(self):

        # Creating GUI - with ttkbootstrap library
        self.__root = ttk.Window(
            themename="vapor", minsize=(1100, 375), maxsize=(1100, 375))

        self.__passsword = None
        self.__is_generated = False
        self.__password_str = StringVar()
        self.__root.title("Password manager-PRO")
        self.__root.iconbitmap("ico.ico")

        self.__pass_len = StringVar()
        self.__username = StringVar()
        self.__website = StringVar()

        self.__uppercase_ = IntVar()
        self.__lowercase_ = IntVar()
        self.__symbols_ = IntVar()
        self.__digits_ = IntVar()

        row = 0
        column = 0
        font = "Rubik Iso"
        size = 12

        # Creating labels that inform about diffrent characters usage
        ttk.Label(text="Include uppercase letters! (e.g. ABCD):", font=(font, size)).grid(
            sticky='W', row=row, column=column, pady=15, padx=5)
        row += 1
        ttk.Label(text="Include lowercase letters! (e.g. abcd):", font=(font, size)).grid(
            sticky='W', row=row, column=column, pady=15, padx=5)
        row += 1
        ttk.Label(
            text="Include symbols case letters! (e.g. .></):", font=(font, size)).grid(sticky='W', row=row, column=column, pady=10, padx=5)
        row += 1
        ttk.Label(text="Include digits letters! (e.g. 4567):", font=(
            font, size)).grid(sticky='W', row=row, column=column, pady=15, padx=5)
        row += 1

        # Creating input to display, edit and write password
        self.__password_input = ttk.Entry(
            state="disabled", bootstyle="info",  width=40, textvariable=self.__password_str)
        self.__password_input.grid(
            sticky='W', row=row, column=column, pady=15, padx=5)

        row = 0
        column += 1

        # Creating checkbuttons for diffrent regimes
        self.__checkb_uppercase = ttk.Checkbutton(
            bootstyle="success-round-toggle", variable=self.__uppercase_)
        self.__checkb_uppercase.grid(
            sticky='W', row=row, column=column)

        row += 1
        self.__checkb_lowercase = ttk.Checkbutton(
            bootstyle="success-round-toggle", variable=self.__lowercase_)
        self.__checkb_lowercase.grid(
            sticky='W', row=row, column=column)

        row += 1
        self.__checkb_symbols = ttk.Checkbutton(
            bootstyle="success-round-toggle", variable=self.__symbols_)
        self.__checkb_symbols.grid(
            sticky='W', row=row, column=column)

        row += 1
        self.__checkb_digits = ttk.Checkbutton(
            bootstyle="success-round-toggle", variable=self.__digits_)
        self.__checkb_digits.grid(
            sticky='W', row=row, column=column)

        row += 1
        ttk.Button(bootstyle="success-outline", text="Copy", width=5, command=self.copy_to_clipboard).grid(
            sticky='W', row=row, column=column)

        # Creating labels to inform about necessery entries
        row = 0
        column += 1
        ttk.Label(
            text="Enter your username: ", font=(font, size)).grid(
            sticky='E', row=row, column=column, pady=10, padx=70)
        row += 1
        ttk.Label(text="Website link: ",  font=(font, size)).grid(
            sticky='E', row=row, column=column, pady=10, padx=70)

        row += 1
        ttk.Label(text="Number of characters: ", font=(font, size)).grid(
            sticky='E', row=row, column=column, pady=10, padx=70)
        row = 0

        # Entries -> username, website adress, number of charcters
        column += 1
        self.__username_input = ttk.Entry(
            state="enabled", bootstyle="info",  width=40, textvariable=self.__username)
        self.__username_input.grid(
            sticky='W', row=row, column=column, pady=10)
        row += 1

        self.__website_input = ttk.Entry(
            state="enabled", bootstyle="info",  width=40, textvariable=self.__website)
        self.__website_input.grid(
            sticky='W', row=row, column=column, pady=10)

        row += 1

        self.__pass_len_input = ttk.Entry(
            state="enabled", bootstyle="info",  width=40, textvariable=self.__pass_len)
        self.__pass_len_input.grid(
            sticky='W', row=row, column=column, pady=10)

        # Buttons
        row += 1
        ttk.Button(text="GENERATE", bootstyle="success-outline", width=30, command=self.generate_password).grid(
            row=row, column=column)
        row += 1
        ttk.Button(text="SAVE PASSWORD", bootstyle="info-outline", command=self.save_password, width=30).grid(
            row=row, column=column)
        row += 1
        ttk.Button(text="SHOW PASSWORDS", bootstyle="warning-outline", command=self.show_passwords, width=30).grid(
            row=row, column=column)

        self.__root.mainloop()


if __name__ == "__main__":
    App()
