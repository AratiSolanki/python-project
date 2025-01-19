'''Question 15
Level 2

Write a program that computes the value of a+aa+aaa+aaaa with
a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.'''


a = input("Enter a digit: ")
n1 = int(a)#9
n2 = int(a * 2)#9*9=81
n3 = int(a * 3)#9*9*9=279
n4 = int(a * 4)#9*9*9*9=6561
result = n1 + n2 + n3 + n4
print(result)


