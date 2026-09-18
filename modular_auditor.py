stock_quantity = 0
Failed=0
Inventory=0
def get_valid_input(Failed):
            stock_quantity = input("Enter the stock quantity: ")
            try:
                    if stock_quantity=="quit":
                        return stock_quantity,Failed
                    if int(stock_quantity) < 0:
                        print("Invalid input. Stock quantity cannot be negative")
                        Failed += 1
                    else:
                            return stock_quantity,Failed
            except ValueError:
                    print("Invalid input. Please enter a valid stock quantity")
                    Failed += 1
                    return get_valid_input(Failed)

def process_delivery(Inventory,stock_quantity):
            Inventory += int(stock_quantity)
            print("New Total inventory:", Inventory)
            if Inventory > 500:
                print("Inventory limit exceeded. Cannot add more stock.")
                return Inventory,True
            return Inventory,False
      
while stock_quantity !="quit":
 stock_quantity,Failed=get_valid_input(Failed)
 print("Quantity entered:", stock_quantity)
 print("Number of Failed entries:", Failed)
 Inventory=process_delivery(Inventory,stock_quantity)
 
