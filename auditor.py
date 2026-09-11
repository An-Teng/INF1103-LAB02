stock_quantity = 0
while stock_quantity !="quit":
    stock_quantity = input("Enter the stock quantity")
    if stock_quantity.isdigit()== True:
        stock_quantity = int(stock_quantity)
        print("Stock quantity entered:", stock_quantity)
    elif stock_quantity.isdigit() == False:
        print("Invalid input. Please enter a valid stock quantity")
    

