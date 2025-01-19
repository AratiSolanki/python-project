'''Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a
console input.'''


#def find_even_digit_numbers():
even_digit_numbers = []
    
for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        even_digit_numbers.append(num_str)
    
print(",".join(even_digit_numbers))

# Call the function
#find_even_digit_numbers()

