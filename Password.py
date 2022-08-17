# Practice portfolio project: Begginer level
# Project idea: GUI for password manager and generator
# Author: Milos Marinkovic
import random
import string
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet


class Password():

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __init__(self, web_link, username, password_length, digits=False, uppercase=False, lowercase=True, symbols=False):

        self.__web_link = web_link
        self.__useraname = username
        self.__password_length = password_length
        self.__digits = digits
        self.__uppercase = uppercase
        self.__lowercase = lowercase
        self.__symbols = symbols
        with open('passkey.key', 'rb') as passkey:
            self.__key = passkey.read()
        self.__fernet = Fernet(self.__key)

        self.__password = ""
        self.__encrypted_password = ''

    def encrpyt_password(self):
        return self.__fernet.encrypt(self.__password.encode())

    def decrpyt_password(self):
        return self.__fernet.decrypt(self.__encrypted_password.encode())

    def generate_password(self):
        password_container = []
        if self.__digits:
            password_container.append(string.digits)
        if self.__uppercase:
            password_container.append(string.ascii_uppercase)
        if self.__lowercase:
            password_container.append(string.ascii_lowercase)
        if self.__symbols:
            password_container.append(string.punctuation.replace("&", ""))

        for _ in range(self.__password_length):
            char_type_index = random.randint(0, len(password_container) - 1)
            self.__password += password_container[char_type_index][random.randint(
                0, len(password_container[char_type_index]) - 1)]

    def save_password(self):
        tree = ET.parse('passwords.xml')
        root = tree.getroot()

        password_to_save = ET.Element("password")
        password_to_save.text = self.encrpyt_password().decode()
        password_to_save.set('username', self.__useraname)
        password_to_save.set('web-page', self.__web_link)
        root.append(password_to_save)

        tree.write('passwords.xml')

    def read_password(self):
        tree = ET.parse('passwords.xml')
        root = tree.getroot()

        self.__encrypted_password = root.find(
            ".//password[@username='{}']".format(self.__useraname)).text
