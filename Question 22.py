'''Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question,
it should be assumed to be a console input.'''


def word_frequency(text):
    word_list = text.split()
    frequency_dict = {}
    
    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    sorted_frequency_dict = dict(sorted(frequency_dict.items()))
    
    for word, frequency in sorted_frequency_dict.items():
        print(f"{word}:{frequency}")

# Sample input
input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_frequency(input_text)


