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
        # My mother actually told me I should have a list of letters guessed that weren't in the phrase
        # So I added that in, even though I know it has nothing to do with the requirements I thought
        # It would be a great addition to the program for the users sake!
        missed_letters_guessed = []
        for letter in guesses:
            if letter not in self.phrase:
                missed_letters_guessed.append(letter)
        print("\nMissed letters you guessed already:")
        print(", ".join(missed_letters_guessed))

    # Checking if the letter guessed is in the phrase
    def check_letter(self, guess):
        return guess in self.phrase

    # Checking to see if the whole phrase has been guessed
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
