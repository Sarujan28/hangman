# Class called Hangman
import random
class Hangman:
    '''
    The class is used to create a game of Hangman that chooses a word
    from a list specified by the user.
     
    Attributes:
        word_list (list): list of words
        num_lives (int): number of lives user has, default number of lives
                         is five when no value is specified in parameters
    '''

    def __init__(self, word_list = None, num_lives = None):
        '''
        See help(Hangman) for accurate signatures

        Other variables intialised:
            word (str): random word chosen from list specified in parameters
                        of Hangman class
            word_guessed (list): list of underscores that will be replaced
                                 by correct guesses
            num_letters (int): number of guesses left to complete random word
            list_of_guesses (list): list of guesses made by user
        '''
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
        '''
        This function is used to check if the guess is in the word. If correct, number
        of letters left to guess is reduced and letter added to the guess. If incorrect, 
        number of lives reduced by one.

        Args:
            guess: single aplhabetical input given by user                 
        '''
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
        '''
        This function is used to check the validity of the input given. The
        input being valid means it is a singular alphabetical letter that has
        not already been guessed.
        '''
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
        '''
        This function is used to play the game. The game continues until zero lives
        are reached where the user loses the game or there are more than 0 lives
        and there are no letter of the word left to be guessed where the user wins
        the game.

        Args:
            word_list (list): list of words
        '''
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