import sys
import random
from phrasehunter.phrase import Phrase


class Game:
    # Creating the initializer for our Game class
    def __init__(self):
        # Setting the missed attribute to 0
        self.missed = 0
        # Setting the phrase attribute with phrases for our game
        self.phrases = [
            Phrase("phrase hunter game"),
            Phrase("python is awesome"),
            Phrase("happy coding everyone"),
            Phrase("tech degree project three"),
            Phrase("object oriented python")
        ]
        # Setting the activate_phrase attribute to get a random phrase when our
        # game starts
        self.activate_phrase = self.get_random_phrase()
        # Setting the guesses attribute with an empty list
        self.guesses = [" "]

    # Creating the start game method to start upon running the program
    def start(self):
        # Calling our welcome message at the start of the game
        self.welcome()
        while self.game_over() == False:
            print("\nYou have missed {} out of 5.".format(self.missed))
            # Calling the activate_phrase to display with underscores
            self.activate_phrase.display(self.guesses)
            self.get_guess()

    # Creating a method and setting a variable to randomize the phrases at the
    # start of the game
    def get_random_phrase(self):
        # randomizing our phrases for the game
        shuffle_phrase = random.choice(self.phrases)
        return shuffle_phrase

    # Creating a method to display a welcome message to our user. I've added
    # some info on how to play the game for the user
    def welcome(self):
        # Welcome message to the player along with instructions on how to play
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
        guess = input("\nPick a letter you think is in the phrase: ")
        if self.activate_phrase.check_letter(guess) == False:
            self.missed += 1
            if len(guess) > 1:
                print("\nOnly pick 1 letter at a time, Try Again!")
                self.missed += 1
            elif not guess.isalpha():
                print("\nInvalid character, use letters only, Try Again!")
                self.missed += 1
            elif len(guess) > 1:
                print("")
                self.missed += 1
        elif guess in self.guesses:
            print("You have already picked that letter, Try Again!")
        self.guesses.append(guess)
        return guess

    # Creating the game_over method and displaying the message according to the
    # outcome of the game
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
            self.keep_playing()
            return True
        else:
            return False

    # Creating a method to prompt the user if they would like to keep playing
    def keep_playing(self):
        keep_playing = input("\nWould you like to pay again? Enter Y or N: ")
        if keep_playing.upper() == "Y":
            Game.start(self)
        elif keep_playing.upper() == "N":
            print("Hope you enjoyed the game! Exiting...")
            sys.exit()
        else:
            print("\nThat was not a valid response. Try Again!")
            return self.keep_playing
