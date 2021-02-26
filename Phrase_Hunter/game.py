from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("phrase hunter game"),
            Phrase("python is awesome"),
            Phrase("happy coding everyone"),
            Phrase("tech degree project three"),
            Phrase("object oriented python")
        ]
        self.activate_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcme()

    def get_random_phrase(self):
        pass

    def welcome(self):
        print("""
        +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
        Welcome To The Phrase Hunter Game!!
        =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
        """)
        print("You are given 5 lives, each missed guess is 1 life.")

    def get_guess(self):
        pass

    def game_over(self):
                print("""\n
        +=+=+=+=+=+=+=+=+=+=+=+=+=+
        - - - - -GAME OVER- - - - -
        =+=+=+=+=+=+=+=+=+=+=+=+=+=
        """)
        play_again = input("Would you like to pay again? Enter Y or N: ")
        if play_again.lower() == "Y":
            Game.start()
        elif play_again.lower() == "N":
            print("Hope you enjoyed the game! Exiting game...")
            sys.exit()
        else:
            print("That was not a valid response. Try Again!")
            print(play_again)
