# Class called Hangman
import random
class Hangman:

    def __init__(self, word_list = None, num_lives = None):
        self.word_list = word_list
        if self.word_list == None:
            self.word_list = []
        self.num_lives = num_lives
        if self.num_lives == None:
            self.num_lives = 5
        word = random.choice(self.word_list)
        self.word = word
        word_guessed = ['_'] * len(word)
        self.word_guessed = word_guessed
        num_letters = len(set(word))
        self.num_letters = num_letters
        list_of_guesses = []
        self.list_of_guesses = list_of_guesses
# Check guess method
    def check_guess(self, guess):
        lower_guess = guess.lower()
        if lower_guess in self.word:
            print(f'Good guess! {lower_guess} is in the word.')
             # Adding correct guesses to word being guessed and reducing number of letters needing to be found
            for letter in self.word:
                if letter == lower_guess:
                    self.word_guessed[self.word.index(lower_guess)] = lower_guess
            self.num_letters -= 1
            print(self.num_letters) #
        else:
            # Reducing number of lives for every wrong guess
            self.num_lives -= 1 # type: ignore # Reducing number of lives for every wrong guess
            print(f'Sorry, {lower_guess} is not in the word. Try again.')
            print(self.num_letters) #
            print(f'You have {self.num_lives} lives left.')
# Ask input method
    def ask_input(self):
        while True:
            print(self.word_guessed) #
            guess = input('Guess a single alphabetical letter: ')
            if len(guess) != 1 and guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses) #
                break
# Play game method
    def play_game(self, word_list):
        while True:
            if self.num_lives == 0:
                print(f'You have {self.num_lives} lives left.')
                print(f'You have lost the game. The word was {self.word}')
                break
            elif self.num_letters > 0:
                self.ask_input()
            else:
                print(f'You have won the game. The word was {self.word}')
                break