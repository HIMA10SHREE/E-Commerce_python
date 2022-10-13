from login import *
from register import *
from Products import *
from Cart_d import *
from payment_info import *

class Home(login,Register,Products,Cart_d,Payment):
    def __init__(self):
        # super().__init__()
        print("===================WELCOME TO E-COMMERCE SITE=====================")
        check = True



        while (check):
            print("1.Register:")
            print("2.Login:")
            print("3.Terms and COnditions")
            print("4.Logout")
            choice = int(input("Chooose a option to continue:"))
            if (choice == 1):
                print("WELCOME TO REGISTRATION".center(60, '*'))
                reg = Register()
                reg.my_func()
                print("WELCOME TO LOGIN PAGE".center(60, '*'))
                log = login()
                log.set_email()

                # def funfilter1(self, string):
                #     # print(self.list1)
                #     for obj in self.list_men:
                #         if string in obj:
                #             print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
                #
                # def funfilter2(self, string):
                #     # print(self.list1)
                #     for obj in self.list_women:
                #         if string in obj:
                #             print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
                #
                # def funfilter3(self, string):
                #     # print(self.list1)
                #     for obj in self.list_kids:
                #         if string in obj:
                #             print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')

                def funmain1():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter1(inp)
                            # funfilter1(self.inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain1()
                        elif bp == 'no':
                            inpu = False

                def funmain2():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter2(inp)
                            # funfilter2(self,inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain2()
                        elif bp == 'no':
                            inpu = False

                def funmain3():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter3(inp)
                            # funfilter3(self.inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain3()
                        elif bp == 'no':
                            inpu = False

                def cart_call():
                    check = True
                    while (check):
                        print("1.Add Items to Cart:")
                        print("2.Go to cart:")
                        # print("3.Order Details")
                        print("3.exit")
                        choice = int(input("Chooose a option to continue:"))
                        if (choice == 1):
                            # product.add_product()
                            cart_info = Cart_d()
                            cart_info.order_details()
                        elif choice == 2:
                            f = open("Cart_details.txt", 'r')
                            cart_read = f.read()
                            print(cart_read)
                            f.close()
                            goto_card=Payment()
                            goto_card.add_grand_total()







                        elif choice == 3:
                            check = False

                check = True
                while (check):
                    print("1.Men's Section")
                    print("2.Women's Section")
                    print("3.Kids' Section")
                    print("4.Exit")

                    choice = int(input("Choose your desired section:"))
                    if (choice == 1):
                        product.get_data1()
                        funmain1()
                        # cart_info = Cart_d()
                        cart_call()
                        # cart_info.add_product()

                    elif choice == 2:
                        product.get_data2()
                        funmain2()
                        # cart_info = Cart_d()
                        # cart_info.add_product()
                        cart_call()

                    elif choice == 3:
                        product.get_data3()
                        funmain3()
                        # cart_info = Cart_d()
                        # cart_info.add_product()
                        cart_call()

                    elif choice== 4:
                        break



            elif choice == 2:
                print("WELCOME TO LOGIN PAGE".center(60, '*'))
                log = login()
                log.set_email()
                #log.set_password()
                def funmain1():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter1(inp)
                            # funfilter1(self.inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain1()
                        elif bp == 'no':
                            inpu = False

                def funmain2():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter2(inp)
                            # funfilter2(self,inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain2()
                        elif bp == 'no':
                            inpu = False

                def funmain3():
                    inpu = True
                    global inp
                    while inpu:
                        print("1.What do you want?:")

                        choice = int(input("Enter option:"))
                        if choice != 1:
                            pass
                        else:
                            inp = input("Enter input:")
                            product.funfilter3(inp)
                            # funfilter3(self.inp)
                        # elif choice == 2:
                        #     inp = input("Enter Room Type:")
                        #     a.funfilter(inp)
                        # elif choice==3:
                        #     inp=int(input("Enter Room price:"))
                        print("\nDo u want to search again[yes/no]")
                        bp = input()
                        if bp == 'yes':
                            funmain3()
                        elif bp == 'no':
                            inpu = False

                def cart_call():
                    check = True
                    while (check):
                        print("1.Add Items to Cart:")
                        print("2.Go to cart:")
                        # print("3.Order Details")
                        print("3.exit")
                        choice = int(input("Chooose a option to continue:"))
                        if (choice == 1):
                            # product.add_product()
                            cart_info = Cart_d()
                            cart_info.order_details()
                        elif choice == 2:
                            f = open("Cart_details.txt", 'r')
                            cart_read = f.read()
                            print(cart_read)
                            f.close()
                            goto_card=Payment()
                            goto_card.add_grand_total()







                        elif choice == 3:
                            check = False

                check = True
                while (check):
                    print("1.Men's Section")
                    print("2.Women's Section")
                    print("3.Kids' Section")
                    print("4.Exit")

                    choice = int(input("Choose your desired section:"))
                    if (choice == 1):
                        product.get_data1()
                        funmain1()
                        # cart_info = Cart_d()
                        cart_call()
                        # cart_info.add_product()

                    elif choice == 2:
                        product.get_data2()
                        funmain2()
                        # cart_info = Cart_d()
                        # cart_info.add_product()
                        cart_call()

                    elif choice == 3:
                        product.get_data3()
                        funmain3()
                        # cart_info = Cart_d()
                        # cart_info.add_product()
                        cart_call()

                    elif choice ==4:
                        break


            elif choice ==3:
                f = open("Terms.txt", 'r')
                data = f.read()
                print(data)
                print('\n')
            elif choice == 4:
                check = False


h = Home()