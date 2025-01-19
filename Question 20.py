'''Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield'''
res=[]
n=int(input("Enter The Number : "))
for i in range(0,n):
    if i % 7 == 0 :
        res.append(str(i))
print(",".join(res))

