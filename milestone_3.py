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