import random

word_list = ['apple', 'banana', 'cherry', 'date']

print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Please input your first guess as a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print( "Oops! That is not a valid input.")