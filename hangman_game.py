import random

from text_data import text_data
from word_data import word_data
from penalty import penalty_instance

maxNumberOfGuesses = 7
wrongGuessCount = 0
guessedLetters = []



def UpdatedWord(word, guessed_Letters):
    updated_word = ""
    for letter in word:
        if letter.upper() in guessed_Letters:
            updated_word += letter + " "
        else:
            updated_word += "_ "
    return updated_word.strip()


  #To Do:
  # - Add while loop to continue game
    
class hangman_game:
    textObj = text_data()
    wordData = word_data()
    
   
    textObj.greeting()

    #get the random word
    Randomly_Selected_Word = random.choice(wordData.wordList)

    #Todo: Show the underscored word
    print(textObj.underScore(Randomly_Selected_Word))

    #verify user input is a letter
    # check if they already used it

   #  loop to continue game
    while wrongGuessCount < maxNumberOfGuesses:
      userLetter = input("Please enter a letter: ").upper()
      userLetter = userLetter[0]

      while not wordData.isLetter(userLetter) or userLetter.upper() in guessedLetters:
        userLetter = input("You did not type a letter or you already guessed it! Please type another letter: ")
        userLetter = userLetter[0]


      #store userletter in guessed letters
      guessedLetters.append(userLetter)


      #Todo: check if userletter is in the guessed word
      #if true, print something
      #else print something else
      if userLetter in Randomly_Selected_Word.upper():
        print("Good guess! The letter " + userLetter + " is in the word.")
        print(UpdatedWord(Randomly_Selected_Word, guessedLetters))
      else:
        print(userLetter + " is not in the word.")
        penalty_instance.draw_hangman(wrongGuessCount)
        wrongGuessCount += 1

      if UpdatedWord(Randomly_Selected_Word, guessedLetters) == Randomly_Selected_Word:
        break

            # end while loop
         
