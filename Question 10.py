'''Question 10
Level 2

Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to
be a console input.
We use set container to remove duplicated data automatically and
then use sorted() to sort the data.
'''

def remove_duplicates_and_sort():
    input_string = input("Enter a sequence of words: ")
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    print(" ".join(sorted_words))

# Call the function
remove_duplicates_and_sort()
