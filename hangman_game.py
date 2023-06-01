import random

from text_data import text_data
from word_data import word_data
from penalty import penalty_instance

maxNumberOfGuesses = 7
wrongGuessCount = 0
guessedLetters = []
userUpdatedWord = []


def UpdatedWord(word, userLetterGuess):

    for n in range(len(word)):
         if(userLetterGuess == word[n]):
             userUpdatedWord[n] = userLetterGuess




    
class hangman_game:
    textObj = text_data()
    wordData = word_data()
    
   
    textObj.greeting()

    #get the random word
    Randomly_Selected_Word = random.choice(wordData.wordList).upper()

    userUpdatedWord = textObj.underScore(Randomly_Selected_Word)

    print(userUpdatedWord + "is the word and the length is " + str(len(userUpdatedWord)))

    #verify user input is a letter
    # check if they already used it

   #  loop to continue game
    while wrongGuessCount<=7:
      userLetter = input("Please enter a letter: ").upper()
      userLetter = userLetter[0]

      while ((wordData.isLetter(userLetter) == False) and (userLetter.upper() not in guessedLetters)):
         userLetter = input("You did not type a letter or you already guessed it! Please type another letter!")
         userLetter = userLetter[0]


      #store userletter in guessed letters
      guessedLetters.append(userLetter)


      #Todo: check if userletter is in the guessed word
      #if true, print something
      #else print something else
      if userLetter in Randomly_Selected_Word.upper():
         print("Good Guess the letter "+userLetter+" is in the word")
         #   print updated word
         UpdatedWord(Randomly_Selected_Word,userLetter)
      else:
         print(userLetter+" is not in the word")
         penalty_instance.draw_hangman(wrongGuessCount)

      print(userUpdatedWord + "is the Updated user word! ")
      wrongGuessCount+=1
      # end while loop
   
