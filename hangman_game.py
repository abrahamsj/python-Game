import random
from text_data import text_data
from word_data import word_data
from penalty import Penalty

maxNumberOfGuesses = 7

def UpdatedWord(word, guessed_letters):
    updated_word = ""
    for letter in word:
        if letter.upper() in guessed_letters:
            updated_word += letter + " "
        else:
            updated_word += "_ "
    return updated_word.strip()

class HangmanGame:
    def __init__(self):
        self.textObj = text_data()
        self.wordData = word_data()
        self.penalty_instance = Penalty()

    def play_game(self):
        self.textObj.greeting()

        play_again = True

        while play_again:
            # Get a random word
            randomly_selected_word = random.choice(self.wordData.wordList)

            # Initialize game variables
            wrong_guess_count = 0
            guessed_letters = []

            print(self.textObj.underScore(randomly_selected_word))

            # Loop to continue the game
            while wrong_guess_count < maxNumberOfGuesses:
                user_letter = input("Please enter a letter: ").upper()
                user_letter = user_letter[0]

                while not self.wordData.isLetter(user_letter) or user_letter.upper() in guessed_letters:
                    user_letter = input("You did not type a letter or you already guessed it! Please type another letter: ")
                    user_letter = user_letter[0]

                # Store user letter in guessed letters
                guessed_letters.append(user_letter)

                if user_letter in randomly_selected_word.upper():
                    print("Good guess! The letter " + user_letter + " is in the word.")
                    print(UpdatedWord(randomly_selected_word, guessed_letters))
                else:
                    print(user_letter + " is not in the word.")
                    self.penalty_instance.draw_hangman(wrong_guess_count)
                    wrong_guess_count += 1

                if UpdatedWord(randomly_selected_word, guessed_letters) == randomly_selected_word:
                    print("Congratulations! You guessed the word correctly.")
                    break

            # Check if the game ended
            if wrong_guess_count == maxNumberOfGuesses:
                print("You reached the maximum number of guesses. The word was: " + randomly_selected_word)
            elif UpdatedWord(randomly_selected_word, guessed_letters) == randomly_selected_word:
                print("Congratulations! You guessed the word correctly.")

            # Check if the player wants to play again
            play_again_input = input("Do you want to play again? (Y/N): ").upper()
            play_again = play_again_input == "Y"

        print("Thank you for playing!")

# Create an instance of HangmanGame and play the game
game = HangmanGame()
game.play_game()
