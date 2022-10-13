from register import *




class login(Register):
    def __init__(self, email="", password=""):
        super().__init__()
        self.email = email
        self.password = password

    def set_email(self):
        while True:
            email = input("Enter email:")
            # if email in passwordlist.keys():
            #     self.email = email
            f = open("User_Data.txt", 'r')
            info = f.read()
            info = info.split()
            if email in info:
                index = info.index(email) + 1
                usr_password = info[index]
                while True:
                    password = input("Enter password:")
                    if usr_password == password:
                        print("Welcome Back, ")
                        break
                    else:
                        print("Password entered is wrong")

                break
            else:
                print("Not a registered account")











