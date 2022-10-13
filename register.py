import re

passwordlist = {}



# print("1.Registration or Signup")
# print("2.Login")


class Register:

    #def __init__(self):

    def my_func(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            e_mail = input("Enter email id:")
            if (re.fullmatch(regex, e_mail)):
                #passwordlist.add(e_mail)
               # emailcheck += e_mail
                f = open("User_Data.txt", 'r')
                info = f.read()
                if e_mail in info:
                    print("E_mail Unavailable. Please Try Again")
                    continue
                f.close()

                f = open("User_Data.txt", 'w')
                info = info + " " + e_mail
                f.write(info)
                f.close()
                print("Email saved")
                print(
                    "password format:\n   atleast 1  [a-z], 1 [A-Z],1 [!%*$#@],1 [0-9]\n   Minimum 6,max 12 character")
                while True:
                    password = input("Enter password:")
                    length = True if len(password) > 6 and len(password) < 13 else False
                    spec_char = ['@', '#', '$', '%', '!', '*']
                    digit = any(char.isdigit() for char in password)
                    is_upper = any(char.isupper() for char in password)
                    is_lower = any(char.islower() for char in password)
                    is_spec_char = any(char in spec_char for char in password)
                    isValid = all([length, digit, is_upper, is_lower, is_spec_char])
                    if isValid:
                       # passwordlist[e_mail] = password
                       f = open("User_Data.txt", 'w')
                       if e_mail in info:
                           info=info+ " "+ password
                           f.write(info)
                       f.close()
                       print("Password saved")
                       break
                    else:
                        print("Enter according to the format")

                break



            else:
                print("Not a valid email")






