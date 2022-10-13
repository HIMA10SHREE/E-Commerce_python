
from enum import Enum,auto
import math


class Order():


    def order_details (self):
        self.T_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
        print("Order placed successfully")
        print(self.c_id)
        print(self.T_id)
        print(self.c_name)
        print(self.c_size)
        print(self.c_price)