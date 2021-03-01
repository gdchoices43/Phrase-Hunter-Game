class Phrase:
    # Creating the initializer for the phrase class
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    # Creating the display for the user to see underscores of the phrase that has not been
    # guessed yet and inserting letters in the phrase if they have been guessed correctly
    def display(self, guesses):
        phrase_display = []
        for letter in self.phrase:
            if letter in guesses:
                phrase_display.append(letter)
            elif letter == " ":
                phrase_display.append(" ")
            else:
                phrase_display.append("_")
        print("\n")
        print(" ".join(phrase_display))

    # Checking if the letter guessed is in the phrase
    def check_letter(self, guess):
        for letter in self.phrase:
            if guess.lower == letter:
                return True
            else:
                return False

    # Checking to see if the whole phrase has been guessed
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
