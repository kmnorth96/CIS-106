#used to access the ceil method to round up
import math

def wall_sqft(length, width, height):

    wall_square_footage = (2 * length * height) + (2 * width * height) 
    paint_needed = math.ceil(wall_square_footage / 50)

    return paint_needed

choice = "yes"

while choice == "yes":

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    paint =  wall_sqft(length, width, height)

    print("Number of gallons needed is: {}".format(paint))

    choice = input("Do you want to run the program again?(yes/no)").lower()