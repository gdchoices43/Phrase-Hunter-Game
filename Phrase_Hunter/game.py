import sys
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
                if len(guess) > 1:
                    print("\nONE LETTER AT A TIME, Try Again")
                elif len(guess) == 0:
                    print("\nINPUT WAS EMPTY, Try Again")
    # Got the isalpha() solution from
    # https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-letters-in-python
                elif guess.isalpha() == False:
                    print("\nUSE LETTERS ONLY, Try Again")
                self.guesses.append(guess)
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
        print("I've made 5 phrases, one was picked at random at the start of the game.")
        print("You pick 1 letter at a time to guess the phrase before your lives run out.")
        print("If you guess a letter in the phrase and there is multiples they will also")
        print("appear. You are given 5 lives, each missed guess is -1 life. Good Luck!")

    # Creating the method to prompt the user to guess a letter in the phrase
    def get_guess(self):
        prompt = input("\nGuess a letter: ")
        return prompt

    def game_over(self):
        if self.activate_phrase.check_complete(self.guesses) == True:
            print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  CONGRATULATIONS! YOU WON PHRASE HUNTER!
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
            """)
            self.activate_phrase.display(self.guesses)
            self.keep_playing()
            return True
        elif self.missed == 5:
            print("""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
- - - - - - -!!GAME OVER!!- - - - - - -
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

-*-*-*-YOU HAVE RAN OUT OF LIVES-*-*-*-
            """)
            self.activate_phrase.display(self.guesses)
            self.keep_playing()
            return True
        else:
            return False

    def keep_playing(self):
        while True:
            try:
                keep_playing = input("\nWould you like to pay again? Enter Y or N: ")
                if keep_playing.upper() == "Y":
                    game = Game()
                    game.start()
                elif keep_playing.upper() == "N":
                    print("\nHope you enjoyed the game! Exiting...")
                    sys.exit()
            except ValueError:
                return self.keep_playing
