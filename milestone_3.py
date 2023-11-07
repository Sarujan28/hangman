# Iterating loop to check if guess input is valid
while True:
    guess = input('Guess a single alphabetical letter: ')
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
        continue
# Check if guess is in the word
import random
word_list = ['orange', 'apple', 'mango', 'melon', 'pear']
word = random.choice(word_list)
if guess in word:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry, {guess} is not in the word. Try again.')
# Check guess function
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
# Ask input function
def ask_input():
    
    import random
    word_list = ['orange', 'apple', 'mango', 'melon', 'pear']
    word = random.choice(word_list)
    
    while True:
        guess = input('Guess a single alphabetical letter: ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue
    
    def check_guess(guess):
        lower_guess = guess.lower()
        if lower_guess in word:
            print(f'Good guess! {lower_guess} is in the word.')
        else:
            print(f'Sorry, {lower_guess} is not in the word. Try again.')
     
    check_guess(guess)