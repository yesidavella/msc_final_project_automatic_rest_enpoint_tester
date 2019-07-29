class Foo:                # Declare a class with a method
    def bar(self, x):
        return 2 * x      # Duplicate x and return it

def main():
    foo = Foo()           # Create an instance of Foo
    print(foo.bar(32))    # Call the bar method and print the result

main()