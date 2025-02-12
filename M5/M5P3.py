#input for total number of books and book cost
books = float(input("Enter number of books to order: "))
cost = float(input("Enter cost per book: "))
#calculate total cost
total = books * cost
#condition to determine shipping costs
if total > 50:
    shipping = 0
else:
    shipping = 25
#display order total and shipping costs
print("Order Total: ${:.2f}".format(total + shipping))
print("Shipping Cost: {}".format(shipping))