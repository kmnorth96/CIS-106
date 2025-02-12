#create inputs for required parameters
name = input("Enter appliance name: ")
cost = float(input("Enter cost of appliance: "))
#conditional to cost and determine warranty percentage
if cost > 1000:
    warranty = .10
else:
    warranty = .05
#calculate warranty total and total cost
warranty_total = cost * warranty
total = cost + warranty_total
#display appliance name, cost, warranty cost, and total cost
print("Appliance Name: {}".format(name))
print("Appliance Cost: ${:.2f}".format(cost))
print("Warranty Cost: ${:.2f}".format(warranty_total))
print("Total Cost: ${:.2f}".format(total))
