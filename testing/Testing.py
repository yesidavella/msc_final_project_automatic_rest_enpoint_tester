from testing.Cat import Cat
import auger

#
#class Testing:
 #   def __init__(self, something):
 #       self.something = something
#    def bark(self):
#        self.something.bark()
#
# ////////////////////////////////////////////////////////////////////////////////////////////


def main():
    cat = Cat("misifoo", 5)           # Create an instance of Foo
    print(cat.calculate_cat_human_years(5))    # Call the bar method and print the result




with auger.magic([Cat]):
    main()