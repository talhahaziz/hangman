# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer picks a random word and the user tries to guess it with a select amount of lives.

## Milestone 1

- I created the remote repository on github and intialised a folder on my local device 
- Connected the remote repository to the local clone using the command line below.

```bash
git clone https://github.com/talhahaziz/hangman
```
## Milestone 2

- Defined the selection of words as word_list 

- Using the import random python library to randomly select a word from the list and assign it to the variable 'word'

```bash 
import random 

word = random.choice(word_list)
```

- takes a character input as the first guess. The input is validated using an if else statement ensuring it is alphabetical and == 1 
 

 ```bash 

guess = input('Please input your first guess as a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print( "Oops! That is not a valid input.")

```

## Milestone 3 

- Create a while loop to continously ask the user to input a letter and validate it with the random word.

- While loop condition is set to True. This is to make sure the code is run continuously.

```bash 
def ask_for_input():
    while True:
        guess = input('Please input your first guess as a single letter: ')

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print( "That is not a valid input, please enter a single alphabetical character.")
    
    check_guess(guess)
```

- check_guess() function is used to check the guess is in the word using an if statement shown below

```bash 
def check_guess(guess):
    if guess in word:
        print(f"Good guess {guess} is in the word!")
    else:
        print(f"Sorry {guess} is not in the word.")
```