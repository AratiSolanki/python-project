'''Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it,
    'you can read document online or find some books. But Python has a
    built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents,
    such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__
var = -94
print('Absolute value of integer is:', abs(var))
print(abs.__doc__)

num=35.4
print('Integer number : ',int(num))
print(int.__doc__)'''
    
def print_docs():
    
    print("Documentation for abs():")
    print(abs.__doc__)
    
    print("\nDocumentation for int():")
    print(int.__doc__)
    
    
    try:
        print("\nDocumentation for raw_input():")
        print(raw_input.__doc__)
    except NameError:
        print("\nDocumentation for input():")
        print(input.__doc__)

    
    def custom_function(x):
        """This is a custom function that returns the square of x."""
        return x ** 2
    
    print("\nDocumentation for custom_function():")
    print(custom_function.__doc__)


print_docs()
