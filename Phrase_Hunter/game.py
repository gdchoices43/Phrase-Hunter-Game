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
        self.activate_phrase = None
        self.guesses = 0

    def start(self):
        pass


    def get_random_phrase(self):
        pass

    def welcome(self):
        pass

    def get_guess(self):
        pass

    def game_over(self):
        pass
