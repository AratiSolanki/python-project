'''Question 25.3:
Define a function that can receive two integral numbers in
string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.'''
def sum_of_strings(a,b):
    
    num1 = int(a)
    num2 = int(b)
    
    
    total = num1 + num2
    
    
    print(total)


sum_of_strings("485", "852") 
sum_of_strings("369", "987")  
