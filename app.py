from phrasehunter.game import Game
import sys

if __name__ == "__main__":
    while True:
        game = Game()
        game.start()
        keep_playing = input("\nWould you like to play again? Enter Y or N: ")
        if keep_playing.upper() == "Y":
            continue
        elif keep_playing.upper() == "N":
            print("\nHope you enjoyed the game! Exiting...")
            sys.exit()
        else:
            print("Not a valid response. Exiting...")
            sys.exit()
