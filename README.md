# Hangman

## Table of Contents
1. [Description](#description)
    - [Introduction](#introduction)
    - [milestone_2](#milestone_2)
    - [milestone_3](#milestone_3)
    - [milestone_4](#milestone_4)
    - [milestone_5](#milestone_5)
    - [hangman_rewrite](#hangman_rewrite)
2. [Usage Instructions](#usage-instructions)
3. [File structure of project](#file-structure-of-project)
4. [License Information](#license-information)

## Description

### Introduction

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. The following milestone sections that refer to the python scripts within this repository. These sections give a timeline of each part of the code and their use that builds towards the completion of the Hangman game.

### milestone_2

In this script, the random module is imported to create a way for the computer to think of a word. Using the random.choice() function, a random word is picked from the list of favourite fruits that was created beforehand. This is assigned to a variable called word.

For the user to guess an input, a variable called guess is created, which has been assigned an input function that asks for a singular alphabetical letter. The guess is then checked if it is valid using if statements. The conditons are checking the length and if it is true that it is alphabetical using the .isalpha() function for it being a valid input.

### milestone_3

An iterating loop is used to check if the guess is valid. The condition for the while loop is set to true so that it will infinitely loop as the condition will always be met. The code from mileston_2 that guesses an input is placed within the while loop. If the input is not valid the loop continues. If the input is valid the loop is broken

The guess is checked against the random word chosen by the computer through if statements. The condition for a correct guess is the guess being in the word. This is then turned into a function that checks if the guess is correct where the guess is an argument.

A function that asks for an input is made to incoporate checking the validity of the guess and if it is in the random word chosen. The random module is imported to pick a random word from a list within the function. This is assigned to a variable called word. The iterating loop previously made is also placed within the function to check if the input is valid. The checking the guess function is nested within ask for input function. The checking the guess function is called within the ask for input function to the end.

### milestone_4

A new class is created called Hangman to create objects from which a game of hangman can be played. In the __ init __() function, two paramaters are initalised being a list of words and number of lives. Both are assigned the value None. This is because the number of lives can be given a default value of 5. Whilst for the list of words, it is set to an empty list so a list can be passed through when an instance of this class is made.

The check guess function is turned into a method within the hangman. An input is asked for by a method followed iterating loop checking the validity of the guess. If the input has already been guessed it continues the loop as each guess is added to a list which the letter is checked against. The loop also continues if the guess is invalid. Otherwise, the loop calls the guess check method if the input has not been guessed and is valid. Following, this the guess is appended to a list of guesses already placed by the user.

Under the check guess method a correct guess is added to the word being guessed, which had been intialised with every letter being replaced by an underscore. For an incorrect guess the number of lives ared reduced by one.

### milestone_5

Another method is added that plays the game of hangman that takes in the list of words as an arguement. Within this method, another iterating loop with the condition True is added to infinitely loop until the game is over. If the number of lives reaches 0, the loop is broken and the user loses the game. If the number of letters that remain unguessed is greater than 0, the ask input method is called. The loop within the ask input method is broken when a valid guess is made to check whether the user has won or lost. Otherwise, the user wins the game as the number of lives is greater than 0 and all letters of the random word have been guessed.

### hangman_rewrite

Instead of the play game method being added, the conditions for ending the game are placed within the ask input method. The conditons are placed after the method for checking if the guess is correct is called. If the number of lives is equal to zero, the user loses and the loop is broken. If the list of correct guesses joined together is equal to the random word, the user wins and the loop is broken. Otherwise, the loop continues. This version of the game has an easier to follow output for the user to play the game.

## Usage Instructions

The repository can be moved to the users computer using git clone with the URL for the remote repository.

Once the user has a local repository for the Hangman game, milestone_5.py can be imported to a python file.

In the python file, a list of words can created by the user assigned to a variable from which the computer picks a random word. Afterwards, a instance of the Hangman game can be created from the Hangman class. The variable assigned with a list of words is passed through as a parameter for the instance of the Hangman class. To play a new game call the play game method.

## File structure of project

## License Information


