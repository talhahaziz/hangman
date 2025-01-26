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

```python
import random 

word = random.choice(word_list)
```

- takes a character input as the first guess. The input is validated using an if else statement ensuring it is alphabetical and == 1 
 

 ```python

guess = input('Please input your first guess as a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print( "Oops! That is not a valid input.")

```

## Milestone 3 

- Create a while loop to continously ask the user to input a letter and validate it with the random word.

- While loop condition is set to True. This is to make sure the code is run continuously.

```python 
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

```python
def check_guess(guess):
    if guess in word:
        print(f"Good guess {guess} is in the word!")
    else:
        print(f"Sorry {guess} is not in the word.")
```

## Milestone 4 

- I introduced a class and defined __init__ to initialise the attributes of the class 

```python
def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len((set(self.word)))
    self.wordlist = word_list
    self.num_lives = num_lives
    self.list_of_guesses = []
```
1. **self.word** - is assigned to the random word from the list 

1. **word_guessed** - this creates a list of each letter from the random word as '_' for example if the random word is apple self.word_guessed will be ['_', '_', '_', '_', '_']

1. **num_letters** - this is the length as an integer of each unique letter from the word for example: set(self.world) if the word is "apple" would be {'a', 'p', 'l', 'e'}

1. **wordlist** - this is the word_list thats passed into the function 

1. **num_lives** - this is the number of lives the player has which is set to 5 

1. **list_of_guesses** - this is a list of guesses that have been entered by the user



