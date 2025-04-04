def compute_commission(sales):
    if sales > 100000:
        commission = sales * .10
    else:
        commission = sales * .05
    
    target = sales * .05
    return commission, target



last_name = input("Enter salesperson last name: ")
sales = float(input("Enter total sales: "))

commission, target = compute_commission(sales)

print("Salesperson: {}\nCommssion: {:.2f}\nTarget: {:.2f}\n".format(last_name, commission, target))