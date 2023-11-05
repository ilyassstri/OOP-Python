# magic method

class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        print("Test, aku dipanggil cuy!")

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def __eq__(self, other):
        return self.title == other.title

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price

ilyas = Game("PES 2016", 60)
chika = Game("Barbie 2021", 130)
risa = Game("Barbie 2021", 110)

print(risa == chika)
print(chika > risa)
print(ilyas > risa)
print(ilyas + risa)


