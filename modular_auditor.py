stock_quantity = 0
Failed=0
Processed=0
Inventory=0
def get_valid_input(Failed,Processed):
            stock_quantity = input("Enter the stock quantity: ")
            try:
                    if stock_quantity=="quit":
                        return stock_quantity,Failed,Processed
                    if int(stock_quantity) < 0:
                        print("Invalid input. Stock quantity cannot be negative")
                        Failed += 1
                        return get_valid_input(Failed,Processed)
                    else:
                            Processed += 1
                            return stock_quantity,Failed,Processed
            except ValueError:
                    print("Invalid input. Please enter a valid stock quantity")
                    Failed += 1
                    return get_valid_input(Failed,Processed)

def process_delivery(Inventory,stock_quantity):
            Inventory += int(stock_quantity)
            print("New Total inventory:", Inventory)
            if Inventory > 500:
                print("Inventory limit exceeded. Cannot add more stock.")
                return Inventory
            return Inventory

def calculate_tax(Inventory):
            tax_amount = Inventory * 0.1
            print("Tax amount on current inventory:", tax_amount)
            return tax_amount

def generate_report(Inventory,Processed,Failed):
            print("Total Units Processed:", Processed)
            print("Number of Failed entries:", Failed)
            print("Final Inventory:", Inventory)
while stock_quantity !="quit":
 stock_quantity,Failed,Processed=get_valid_input(Failed,Processed)
 if stock_quantity == "quit":
        break
 else:
    Inventory=process_delivery(Inventory,stock_quantity)
    tax_amount=calculate_tax(Inventory)

generate_report(Inventory,Processed,Failed)

