number_1 = 0
number_2 = 1

for _ in range(20):
    print(number_1)
    next = number_1 + number_2
    number_1 = number_2
    number_2 = next

print()