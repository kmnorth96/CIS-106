part_number = float(input("Enter part number: "))
quantity = float(input("Enter quantity: "))



if part_number == 10 or part_number == 55:
    unit_cost = 1
elif part_number == 99:
    unit_cost = 2
elif part_number == 80 or part_number == 70:
    unit_cost = 3
else:
    unit_cost = 5


total_cost = quantity * unit_cost

print("Part Number: {}\nUnit Cost: {}\nTotal Cost: {}".format(part_number, unit_cost, total_cost))

