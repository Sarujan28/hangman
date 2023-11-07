import random
# List of favourite fruits
word_list = ['orange', 'apple', 'mango', 'melon', 'pear']
print(word_list)
# Picking random fruit from list of favourite fruits
word = random.choice(word_list)
print(word)
# Asking to guess a letter
guess = input('Enter a single letter:')
if len(guess) == 1 and guess.isalpha() == True:
    print('Good Guess!')
else:
    print('Oops! That is not a vaild input.')