class penalty:
    def draw_hangman(self,stages):
        stages = [
            # stage 0
            """
            _____
            |   |
                |
                |
                |
                |
            ____|___
            """,
            # stage 1
            """
            _______
            |     |
            O     |
                  |
                  |
                  |
            ______|___
            """,
            # stage 2
            """
            ______
            |    |
            O    |
            |    |
                 |
                 |
            _____|___
            """,
            # stage 3
            """
            ______
            |     |
            O     |
           /|     |
                  |
                  |
            ______|___
            """,
            # stage 4
            """
            _______
            |     |
            O     |
           /|\    |
                  |
                  |
            ______|___
            """,
            # stage 5
            """
            _______
            |     |
            O     |
           /|\    |
           /      |
                  |
            ______|___
            """,
            # stage6
            """
            ________
            |      |
            O      |
           /|\     |
           / \     |
                   |
            _______|___
            """
        ]
        print(stages[stage])

# Create an instance of the Penalty class
penalty_instance = penalty()

# Test with default stage 0
stage = 0
penalty_instance.draw_hangman(stage)