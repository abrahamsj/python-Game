import random

from text_data import text_data
from word_data import word_data
from penalty import penalty_instance

maxNumberOfGuesses = 7
wrongGuessCount = 0
guessedLetters = []

# function to shown unknown words
def underScore(word):
    unknownWord = '_' * len(word)
    return unknownWord

def UpdatedWord(word,guessedLetters):
    # create variable to hold correct guessed in the order they appear
    updated_word = "" 
    #loop through for to find letter
    for letter in word:
        if letter in guessedLetters:
            updated_word += letter + " "
        else:
            #dhow _ if the letter for that slot wasn't guessed
            updated_word += "_ "
    return updated_word.strip()

  #To Do:
  # - Add while loop to continue game
    
class hangman_game:
    textObj = text_data()
    wordData = word_data()
    
    textObj.MessageFormat('WELCOME!')
    print(textObj.welcome_message)

    textObj.MessageFormat('GAME RULES')

    print(textObj.rules_Of_game)

    #get the random word
    wordToGuess = random.choice(wordData.wordList)

    #Todo: Show the underscored word
    print(underScore(wordToGuess))

    #verify user input is a letter
    # check if they already used it
    userLetter = input("Please enter a letter: ")
    userLetter = userLetter[0]

    while ((wordData.isLetter(userLetter) == False) and (userLetter.upper() not in guessedLetters.upper())):
       userLetter = input("You did not type a letter or you already guessed it! Please type another letter!")
       userLetter = userLetter[0]


    #store userletter in guessed letters
    guessedLetters.append(userLetter)


    #Todo: check if userletter is in the guessed word
    #if true, print something
    #else print something else
    if userLetter in wordToGuess:
        print("Good Guess the letter "+userLetter.upper()+" is in the word")
      #   print updated word
        print(UpdatedWord(wordToGuess,userLetter))
    else:
        print(userLetter+" is not in the word")
        penalty_instance.draw_hangman(wrongGuessCount)
        wrongGuessCount
