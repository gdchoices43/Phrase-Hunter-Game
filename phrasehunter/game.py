import random
from phrasehunter.phrase import Phrase


class Game:
    # Creating the initializer for our Game class
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Hello World"),
            Phrase("Python Is Awesome"),
            Phrase("Happy Coding Everyone"),
            Phrase("Tech Degree Project Three"),
            Phrase("Object Oriented Python")
        ]
        self.activate_phrase = self.get_random_phrase()
        self.guesses = [" "]

    # Creating the start game method to start upon running the program
    def start(self):
        self.welcome()
        while self.missed < 5 and not self.activate_phrase.check_complete(self.guesses):
            print("\nYou have missed {} out of 5 total misses.".format(self.missed))
            self.activate_phrase.display(self.guesses)
            guess = self.get_guess()
            self.guesses.append(guess)
            if not self.activate_phrase.check_letter(guess):
                self.missed += 1
        self.game_over()

    # Creating a method and setting a variable to randomize the phrases at the start of the game
    def get_random_phrase(self):
        shuffle_phrase = random.choice(self.phrases)
        return shuffle_phrase

    # Creating a method to display a welcome message to our user. I've added some info on how to play
    # the game for the user
    def welcome(self):
        print("""
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
            Welcome To The Phrase Hunter Game!!
    +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
        """)
        print("""
I've made 5 phrases, one was picked at random at the start of the game.
You pick 1 letter at a time to guess the phrase before your lives run out.
If you guess a letter in the phrase and there is multiples they will also
appear. You are given 5 lives, each missed guess is -1 life. I have provided
you with an empty list for missed letters guessed. They will appear after a
missed guess, Good Luck!
        """)

    # Creating the method to prompt the user to guess a letter in the phrase
    def get_guess(self):
        guess = input("\nGuess a letter: ")
        if len(guess) > 1:
            print("\nONE LETTER AT A TIME, Try Again")
        # Got the isalpha() solution from
        # https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-letters-in-python
        elif guess.isalpha() == False:
            print("\nUSE LETTERS ONLY, Try Again")
        else:
            print("\nTry Again")
        return guess

    def game_over(self):
        if self.activate_phrase.check_complete(self.guesses) == True:
            print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
 CONGRATULATIONS! YOU GUESSED THE PHRASE!
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
            """)
            return True
        elif self.missed == 5:
            print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
- - - - - - -!!GAME OVER!!- - - - - - -
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

-*-*-*-YOU HAVE RAN OUT OF LIVES-*-*-*-
            """)
            return True
        else:
            return False
