import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len((set(self.word)))
        self.wordlist = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input('Please input your first guess as a single letter: ')

            if len(guess) != 1 and guess.isalpha() == False:
                print( "That is not a valid input, please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already guessed that letter, please try again.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word!")

            for i in range (len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1     
        else:
            print(f"Sorry {guess} is not in the word.")
            self.num_lives -= 1
            print(f"you have {self.num_lives} lives remaining")


def play_game(word_list):

    num_lives = 5 
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("you lost!")
            break 
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations, You have won the game")
            break
            

word_list = ['grape', 'dragonfruit', 'cherry', 'avacado']

play_game(word_list)