import random

from text_data import text_data
from word_data import word_data

maxNumberOfGuesses = 7
guessedLetters = []

class hangman_game:
    textObj = text_data()
    wordData = word_data()

    print(textObj.welcome_message)

    #get the random word
    wordToGuess = random.choice(wordData.wordList)

    #Todo: Show the underscored word

    #verify user input is a letter
    # check if they already used it
    userLetter = input("Please enter a letter")
    userLetter = userLetter[0]

    while ((wordData.isLetter(userLetter) == False) and (userLetter not in guessedLetters)):
       userLetter = input("You did not type a letter or you already guessed it! Please type another letter!")
       userLetter = userLetter[0]


    #store userletter in guessed letters
    guessedLetters.append(userLetter)


    #Todo: check if userletter is in the guessed word
    #if true, print something
    #else print something else