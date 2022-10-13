from payment_info import *
# from Orderdetails import *

import string
import random

from enum import Enum,auto
import math

list_cart = []


class Cart_d(Payment):


    def __init__(self):
        self.list_cart = []


    #

    # def add_product(self):
        print("Do you want to enter item into cart:")
        item = input("Enter Yes/No")
        if item == "Yes" or item == "yes":
            self.c_id = random.randint(100, 300)
            self.c_name = input("Enter type of cloth:")
            self.c_color = input("Enter color:")
            self.c_size = input("Enter size")
            self.c_brand = input("Enter brand")
            self.c_price = input("Enter price")

            f = open("Cart_details.txt", 'a')
            cart_info = str(self.c_id) + ' ' + self.c_name + ' ' + self.c_color + ' ' + self.c_size + ' ' + self.c_brand + ' ' + self.c_price + '\n'
            f.write(cart_info)
            f.close()

        # print("Your order price is:", c_price)

        check=True
        while(True):
            print("Have you made payment?[Yes/No]")
            input_choice=input()
            if(input_choice=='No' or input_choice=='no'):
                Payment.payment_processing(self)
            elif input_choice=="Yes" or input_choice=='yes':
                break

    def order_details(self):
            self.T_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
            print("Order placed successfully")
            print("The order ID is:",self.c_id)
            print("The traction_id is:",self.T_id)
            print("You have order :",self.c_name)
            print("Size:",self.c_size)
            print("Price :",self.c_price)
            print("\n\n")


#
#
# check=True
#
# while (check):
#     print("1.Add Items to Cart:")
#     print("2.Go to cart:")
#     print("3.exit")
#     choice = int(input("Chooose a option to continue:"))
#     if (choice == 1):
#         # ca.add_product()
#         ca = Cart_d()
#
#     elif choice == 2:
#         f = open("Cart_details.txt", 'r')
#         cart_read=f.read()
#         print(cart_read)
#         f.close()
#
#
#     elif choice == 3:
#        check=False

# ca.add_product()
# ca=Cart_d()