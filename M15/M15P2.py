class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90

class Sportcar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.wheels = 'Y'
        self.engine = 'Y'
        self.interior = 'Y'

    def add_wheels(self, option):
        self.wheels = option

    def add_engine(self, option):
        self.engine = option

    def add_interior(self, option):
        self.interior = option

    def updated_price(self):
        price = self.sticker_price
        if self.wheels == 'Y':
            price += 1000.00
        if self.engine == 'Y':
            price += 3000.00
        if self.interior == 'Y':
            price += 2000.00
        return price

car1 = Car('Hyundai', 'Venue', 20000.00)
car2 = Car('Chevrolet', 'Impala', 28000.00)

sportcar1 = Sportcar('Chevrolet', 'Camaro', 75000.00)
sportcar2 = Sportcar('Dodge', 'Challenger', 60000.00)

print("----------Cars----------")
print("{} {} | Sticker Price: ${:.2f} | Discounted Price: ${:.2f}".format(car1.make, car1.model, car1.sticker_price, car1.discount_price()))
print("{} {} | Sticker Price: ${:.2f} | Discounted Price: ${:.2f}".format(car2.make, car2.model, car2.sticker_price, car2.discount_price()))
print("\n---------Sportcars----------")
print("{} {} | Sticker Price: ${:.2f} | Price with Options: ${:.2f}".format(
    sportcar1.make, sportcar1.model, sportcar1.sticker_price, sportcar1.updated_price()))
print("{} {} | Sticker Price: ${:.2f} | Price with Options: ${:.2f}".format(
    sportcar2.make, sportcar2.model, sportcar2.sticker_price, sportcar2.updated_price()))