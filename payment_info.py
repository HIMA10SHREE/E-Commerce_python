# from Cart_d import *
import random
from enum import Enum,auto
import math
import string

list1 = []
list2= []
class Payment:


    def add_grand_total(self):
        sum=0
        f = open("Cart_details.txt", 'r')
        cart_read_4_pay = f.read()
        #print(cart_read_4_pay)
        # i=5
        # for line[i] in cart_read_4_pay:
        #         sum =sum + int(line[i])
        #         i+=5

        l=cart_read_4_pay.split()
        f.close()

        for i in range(5,len(l),6):
            sum=sum+int(l[i])


        print("Your grand total is :" ,sum)



    def generateOTP(self):
        digits = "0123456789"
        OTP = ""

        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]

        return OTP



    def payment_processing(self):
        print("1.Card payment\n2.UPI Payment\n3.Exit")
        self.method = int(input("Enter payment method:"))
        check = True
        while check:
            # print("1.Card payment\n2.UPI Payment\n3.Exit")
            # self.method = input("Enter payment method:")
            if self.method == 1:
                self.card = input("Enter card number:")
                list1.append(self.card)
                self.ph = input("Enter phone number:")
                list1.append(self.ph)
                OTP = self.generateOTP()
                print("Your OTP is", OTP)
                self.otp = int(input("Enter OTP:"))
                list1.append(self.otp)
                break
            elif self.method == 2:
                self.upi = input("Enter UPI number:")
                list2.append(self.upi)
                print("Payment done successfully")
                break
            else:
                check = False




# pay=Payment()
# pay.add_grand_total()