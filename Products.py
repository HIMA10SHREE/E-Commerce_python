from Cart_d import *
from payment_info import *

list_men = []
list_women= []
list_kids =[]

class Products(Cart_d,Payment):
    def __init__(self):
        self.list_men = []
        self.list_women=[]
        self.list_kids = []

    def products(self, pname, pcolor,psize,pbrand,pamount):
        self.pname = pname
        self.pcolor=pcolor
        self.psize=psize
        self.pbrand=pbrand
        self.pamount = pamount


    def save1(self):
        self.list_men.append([self.pname,self.pcolor, self.psize, self.pbrand, self.pamount])


    def save2(self):
        self.list_women.append([self.pname,self.pcolor, self.psize, self.pbrand, self.pamount])


    def save3(self):
        self.list_kids.append([self.pname,self.pcolor, self.psize, self.pbrand, self.pamount])


    def get_data1(self):

        print("=====================MEN SECTION========================")
        for obj in self.list_men:
            print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
        print("\n \n")


    def get_data2(self):
        print("=====================WOMEN SECTION========================")
        for obj in self.list_women:
            print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
        print("\n \n")

    def get_data3(self):
        print("=====================KIDS SECTION========================")
        for obj in self.list_kids:
            print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
        print('\n')

    def funfilter1(self, string):
        # print(self.list1)
        for obj in self.list_men:
            if string in obj:
                print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')

    def funfilter2(self, string):
        # print(self.list1)
        for obj in self.list_women:
            if string in obj:
                print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')


    def funfilter3(self, string):
        # print(self.list1)
        for obj in self.list_kids:
            if string in obj:
                print(obj[0], obj[1], obj[2], obj[3], obj[4], sep='   ')
    #
    # def funmain1():
    #     inpu = True
    #     global inp
    #     while inpu:
    #         print("1.What do you want?:")
    #
    #         choice = int(input("Enter option:"))
    #         if choice != 1:
    #             pass
    #         else:
    #             inp = input("Enter input:")
    #             product.funfilter1(inp)
    #         # elif choice == 2:
    #         #     inp = input("Enter Room Type:")
    #         #     a.funfilter(inp)
    #         # elif choice==3:
    #         #     inp=int(input("Enter Room price:"))
    #         print("\nDo u want to search again[yes/no]")
    #         bp = input()
    #         if bp == 'yes':
    #             funmain1()
    #         elif bp == 'no':
    #             inpu = False
    #
    # def funmain2():
    #     inpu = True
    #     global inp
    #     while inpu:
    #         print("1.What do you want?:")
    #
    #         choice = int(input("Enter option:"))
    #         if choice != 1:
    #             pass
    #         else:
    #             inp = input("Enter input:")
    #             product.funfilter2(inp)
    #         # elif choice == 2:
    #         #     inp = input("Enter Room Type:")
    #         #     a.funfilter(inp)
    #         # elif choice==3:
    #         #     inp=int(input("Enter Room price:"))
    #         print("\nDo u want to search again[yes/no]")
    #         bp = input()
    #         if bp == 'yes':
    #             funmain2()
    #         elif bp == 'no':
    #             inpu = False
    #
    # def funmain3():
    #     inpu = True
    #     global inp
    #     while inpu:
    #         print("1.What do you want?:")
    #
    #         choice = int(input("Enter option:"))
    #         if choice != 1:
    #             pass
    #         else:
    #             inp = input("Enter input:")
    #             product.funfilter3(inp)
    #         # elif choice == 2:
    #         #     inp = input("Enter Room Type:")
    #         #     a.funfilter(inp)
    #         # elif choice==3:
    #         #     inp=int(input("Enter Room price:"))
    #         print("\nDo u want to search again[yes/no]")
    #         bp = input()
    #         if bp == 'yes':
    #             funmain3()
    #         elif bp == 'no':
    #             inpu = False
    #
    # def cart_call():
    #     check = True
    #     while (check):
    #         print("1.Add Items to Cart:")
    #         print("2.Go to cart:")
    #         print("3.exit")
    #         choice = int(input("Chooose a option to continue:"))
    #         if (choice == 1):
    #             # product.add_product()
    #             cart_info = Cart_d()
    #         elif choice == 2:
    #             f = open("Cart_details.txt", 'r')
    #             cart_read = f.read()
    #             print(cart_read)
    #             f.close()
    #             product.add_grand_total()
    #
    #
    #         elif choice == 3:
    #             check = False
    #
    # check = True
    # while (check):
    #     print("1.Men's Section")
    #     print("2.Women's Section")
    #     print("3.Kids' Section")
    #
    #     choice = int(input("Choose your desired section:"))
    #     if (choice == 1):
    #         product.get_data1()
    #         funmain1()
    #         # cart_info = Cart_d()
    #         cart_call()
    #         # cart_info.add_product()
    #
    #     elif choice == 2:
    #         product.get_data2()
    #         funmain2()
    #         # cart_info = Cart_d()
    #         # cart_info.add_product()
    #         cart_call()
    #
    #     elif choice == 3:
    #         product.get_data3()
    #         funmain3()
    #         # cart_info = Cart_d()
    #         # cart_info.add_product()
    #         cart_call()


product = Products()
product.products('Shirt', "Black", "M", 'Turtle', 'Rs 1800')
product.save1()
product.products('Shirt', "Blue", "XL", 'Wrangler', 'Rs 2400')
product.save1()
product.products('Shirt', "Olive", "M", 'Arrow', 'Rs 1600')
product.save1()
product.products('Trouser', "Black", "M", 'Peter_England', 'Rs 2800')
product.save1()
product.products('Skirt', "Black", "M", 'Urbanic', 'Rs 1200')
product.save2()
product.products('Anarkali Kurti', "Yellow", "XL", 'Libas', 'Rs 2700')
product.save2()
product.products('Sharara', "Olive", "S", 'Biba', 'Rs 3600')
product.save2()
product.products('Sharara', "Wine", "S", 'Fabindia', 'Rs 3600')
product.save2()
product.products('Skirt', "Pink", "M", 'Urbanic', 'Rs 800')
product.save3()
product.products('Jogger', "Red", "XS", 'NIKE', 'Rs 970')
product.save3()
product.products('Jeans', "Blue", "S", 'Pepe_Jeans', 'Rs 1200')
product.save3()
product.products('Palazzo', "Maroon", "S", 'W', 'Rs 1200')
product.save3()

#
# def funmain1():
#     inpu = True
#     global inp
#     while inpu:
#         print("1.What do you want?:")
#
#         choice = int(input("Enter option:"))
#         if choice != 1:
#             pass
#         else:
#             inp = input("Enter input:")
#             product.funfilter1(inp)
#         # elif choice == 2:
#         #     inp = input("Enter Room Type:")
#         #     a.funfilter(inp)
#         # elif choice==3:
#         #     inp=int(input("Enter Room price:"))
#         print("\nDo u want to search again[yes/no]")
#         bp = input()
#         if bp == 'yes':
#             funmain1()
#         elif bp == 'no':
#             inpu = False
#
# def funmain2():
#     inpu = True
#     global inp
#     while inpu:
#         print("1.What do you want?:")
#
#         choice = int(input("Enter option:"))
#         if choice != 1:
#             pass
#         else:
#             inp = input("Enter input:")
#             product.funfilter2(inp)
#         # elif choice == 2:
#         #     inp = input("Enter Room Type:")
#         #     a.funfilter(inp)
#         # elif choice==3:
#         #     inp=int(input("Enter Room price:"))
#         print("\nDo u want to search again[yes/no]")
#         bp = input()
#         if bp == 'yes':
#             funmain2()
#         elif bp=='no':
#             inpu=False
#
#
#
# def funmain3():
#     inpu = True
#     global inp
#     while inpu:
#         print("1.What do you want?:")
#
#         choice = int(input("Enter option:"))
#         if choice != 1:
#             pass
#         else:
#             inp = input("Enter input:")
#             product.funfilter3(inp)
#         # elif choice == 2:
#         #     inp = input("Enter Room Type:")
#         #     a.funfilter(inp)
#         # elif choice==3:
#         #     inp=int(input("Enter Room price:"))
#         print("\nDo u want to search again[yes/no]")
#         bp = input()
#         if bp == 'yes':
#             funmain3()
#         elif bp=='no':
#             inpu=False
#
# def cart_call():
#     check=True
#     while (check):
#         print("1.Add Items to Cart:")
#         print("2.Go to cart:")
#         print("3.exit")
#         choice = int(input("Chooose a option to continue:"))
#         if (choice == 1):
#             # product.add_product()
#             cart_info = Cart_d()
#         elif choice == 2:
#             f = open("Cart_details.txt", 'r')
#             cart_read=f.read()
#             print(cart_read)
#             f.close()
#             product.add_grand_total()
#
#
#         elif choice == 3:
#             check=False
#
#
# check=True
# while (check):
#     print("1.Men's Section")
#     print("2.Women's Section")
#     print("3.Kids' Section")
#
#     choice = int(input("Choose your desired section:"))
#     if (choice == 1):
#         product.get_data1()
#         funmain1()
#         # cart_info = Cart_d()
#         cart_call()
#         # cart_info.add_product()
#
#     elif choice == 2:
#         product.get_data2()
#         funmain2()
#         # cart_info = Cart_d()
#         # cart_info.add_product()
#         cart_call()
#
#     elif choice == 3:
#         product.get_data3()
#         funmain3()
#         # cart_info = Cart_d()
#         # cart_info.add_product()
#         cart_call()
#
#










