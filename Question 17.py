'''Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based
a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
Â¡Â­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.
'''

net_amount = 0
print("Enter transactions (D for deposit, W for withdrawal) and type 'END' to finish:")

while True:
    transaction = input()
    if transaction == 'END':
        break
    if not transaction.strip():
        continue
    try:
        trans_type, amount = transaction.split()
        amount = int(amount)
        if trans_type == 'D':
              net_amount += amount
        elif trans_type == 'W':
            net_amount -= amount
    except ValueError:
        print("Invalid input format. Please enter transactions as 'D <amount>' or 'W <amount>'.")

print(f"Net Amount: {net_amount}")






