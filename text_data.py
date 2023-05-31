class text_data:
  welcome_message = "Hello player!\n Hope you enjoy this game of Hangman\n let's begin!\n"
  rules_Of_game = """
    1. Objective: Guess the hidden word or phrase within a limited number of attempts.\n
    2. Correct Guess: Reveals all occurrences of the guessed letter.\n
    3. Incorrect Guess: Results in the drawing of a body part of the hangman.\n
    4. Winning: Guess all letters correctly before running out of guesses.\n
    5. Losing: Run out of guesses before guessing the word or phrase.\n
    6. Penalty: Incorrect guesses may result in drawn body parts and deductions.\n
    7. Repeated Letters: Guessing the same letter again does not penalize.\n
  """

  def MessageFormat(self,text):
    print('=='*len(text))
    print(text)
    print('=='*len(text))

  