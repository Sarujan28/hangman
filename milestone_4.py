# New class called Hangman
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
        else:
            print(f'Sorry, {lower_guess} is not in the word. Try again.')