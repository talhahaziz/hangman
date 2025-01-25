import random

word_list = ['apple', 'banana', 'cherry', 'date']

print(word_list)

word = random.choice(word_list)
print(word)


def ask_for_input():
    while True:
        guess = input('Please input your first guess as a single letter: ')

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print( "That is not a valid input, please enter a single alphabetical character.")
    
    check_guess(guess)

def check_guess(guess):
    if guess in word:
        print(f"Good guess {guess} is in the word!")
    else:
        print(f"Sorry {guess} is not in the word.")


ask_for_input()


