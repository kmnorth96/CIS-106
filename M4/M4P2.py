purchase_price = input("Enter the purchase price per share: ")
stock_price = input("Enter the current stock price: ")
quantity = input("Enter the number of shares: ")

compute_value = (float(stock_price) - float(purchase_price)) * float(quantity)

print("Value:{:.2f}".format(compute_value))