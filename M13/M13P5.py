import math #for rounding

def room_info():
    rooms = []
    while True:
        name = input("Enter room name ortype done to finish: ")
        if name.lower() == "done":
            break
        length = float(input("Enter room length in feet: "))
        width = float(input("Enter room width in feet: "))
        height = float(input("Enter room height in feet: "))
        rooms.append({"name": name, "length": length, "width": width, "height": height})
    return rooms

def calc_paint(rooms):
    paint_needed = {}
    for room in rooms:
      
        area = 2 * (room["length"] + room["width"]) * room["height"]
        gallons = math.ceil(area / 50)
        paint_needed[room["name"]] = gallons

    return paint_needed

def print_paint_info(paint_dict):
    print("\nGallons of Paint Needed per Room")
    print("----------------------------------")
    for room, gallons in paint_dict.items():
        print("{:<15} {} gallon(s)".format(room, gallons))

#run
room_info = room_info()
paint_results = calc_paint(room_info)
print_paint_info(paint_results)