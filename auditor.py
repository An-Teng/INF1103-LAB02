stock_quantity = 0
Inventory=0
Processed=0
Failed=0
while stock_quantity !="quit":
    stock_quantity = input("Enter the stock quantity: ")
    try:
        if int(stock_quantity) < 0:
                    print("Invalid input. Stock quantity cannot be negative")
                    Failed += 1
        elif stock_quantity.isnumeric()== True:
                stock_quantity = int(stock_quantity)
                print("Stock quantity entered:", stock_quantity)
                Processed += 1
                Inventory += stock_quantity
                print("Total inventory:", Inventory)
                if Inventory >500:
                        print("Inventory limit exceeded. Cannot add more stock.")
                        break
                    
        elif stock_quantity.isdigit() == False:
            print("Invalid input. Please enter a valid stock quantity")
            Failed += 1
    except:
        print("Invalid input. Please enter a valid stock quantity")
        Failed += 1
print("Total Units Processed:", Processed)
print("Number of Failed entries:", Failed)
