##BIKE RENTAL SYSTEM??
class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def DisplayBike(self):
        print("Total Bikes",self.stock)

    def RentForBike(self,quantity):
        if quantity<=0:
            print("Enter the Positive value OR Greater than 0")
        elif quantity>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-quantity
            print("Total price",quantity*100)
            print("Total Bikes",self.stock)
while True:
    obj=BikeShop(100)
    user_input=int(input("""
               
            Welcome! To my BIKESTORE
              press(1) To Display Stock
              press(2) To Rent a Bike
              press(3) To Exit
                    """))
    if user_input==1:
        obj.DisplayBike()
    elif user_input==2:
        n=int(input("Enter the Quantity:---"))
        obj.RentForBike(n)
    else:
        break
        