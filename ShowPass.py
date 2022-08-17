import ttkbootstrap as ttk
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet
from ttkbootstrap.constants import *


class ShowPasswords():

    def decrypt_password(self, password):
        with open('passkey.key', 'rb') as passkey:
            key = passkey.read()
        fernet = Fernet(key)
        return fernet.decrypt(password).decode()

    def get_all_passwords(self):
        tree = ET.parse('passwords.xml')
        root = tree.getroot()

        for password in root.iter('password'):
            password.attrib['password'] = self.decrypt_password(
                password.text.encode())
            self.__passwords.append(password.attrib)

    def create_label(self, password):
        color = 'inverse-primary' if self.__alternate else 'inverse-secondary'

        ttk.Label(self.__root, text="User: {:<20}\nLink: {:<20}\nPassword: {:<20}".format(password['username'], password['web-page'], password['password']), style=color,
                  width=600, font=20).pack()
        self.__row += 1
        self.__alternate = not self.__alternate

    def __init__(self):
        self.__passwords = []
        self.__alternate = False
        self.__row = 0
        self.get_all_passwords()

        self.__root = ttk.Window(themename="vapor", minsize=(
            600, 900), maxsize=(600, 900))
        self.__root.title("Passwords")
        self.__root.iconbitmap('ico.ico')

        for password in self.__passwords:
            self.create_label(password)

        self.__root.mainloop()


ShowPasswords()
