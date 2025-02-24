tickets = float(input("Enter number of tickets: "))

if tickets >= 25:
    ticket_price = 50
elif tickets >= 10 and tickets < 25:
    ticket_price = 60 
elif tickets >= 5 and tickets < 10:
    ticket_price = 70
else:
    ticket_price = 75

total_cost = tickets * ticket_price

print("Number of tickets: {}\nTicket Price: {:.2f}\nTotal Cost: {:.2f}".format(tickets, ticket_price, total_cost))