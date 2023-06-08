class Penalty:
    @staticmethod
    def draw_hangman(stage):
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
            # stage 6
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
