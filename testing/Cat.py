class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Miauuuuuuu... re miauuuu!!!")

    def calculate_cat_human_years(self, x):
        z = x *7

        if z <= 0:
            z = 0

        return z