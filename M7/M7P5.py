answer = input("Do you wish to continue the program? ")
discount_sum = 0


if answer == "Yes":
    print("Okay, let's continue")
    while answer == "Yes":
      quantity = float(input("Enter quantity: "))
      price = float(input("Enter price: "))
      
      extended_price = quantity * price
      if extended_price > 10000:
        discount = extended_price *.25
        final_price = extended_price - discount
      else:
        discount = extended_price * .10
        final_price = extended_price - discount



      discount_sum = discount_sum + discount
      print("Extended Price: {}\nDiscount amount: {}\nFinal Price: {}".format(extended_price, discount, final_price))
      answer = input("Do you want to enter another item? ")
    
print("Sum of discounts: ", discount_sum)    

