from phrasehunter.game import game


if __name__ == "__main__":
    play_again = input("Would you like to pay again? Enter Y/N ")
    while True:
        try:
            if play_again.lower() == "Y":
                game = Game()
                game.start()
            else:
                print("I hope you enjoyed the game! Exiting Phrase Hunter Game...")
                sys.exit()
        except ValueError as error:
            print("\nThat was not a valid response. Please try again.\n")
            print(play_again)
