# Iterating loop to check if guess input is valid
while True:
    guess = input('Guess a single alphabetical letter: ')
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
        continue