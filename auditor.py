stock_quantity = 0
Inventory=0
while stock_quantity !="quit":
    stock_quantity = input("Enter the stock quantity: ")
    if int(stock_quantity) < 0:
                print("Invalid input. Stock quantity cannot be negative")
    elif stock_quantity.isnumeric()== True:
            stock_quantity = int(stock_quantity)
            print("Stock quantity entered:", stock_quantity)
            Inventory += stock_quantity
    elif stock_quantity.isdigit() == False:
        print("Invalid input. Please enter a valid stock quantity")
    

