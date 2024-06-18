import game

from blessings import Terminal


def main():
    # clear the terminal window
    term = Terminal()
    print(term.clear())

    # Play the game until the game is over
    game.play_game()



if __name__ == "__main__":
    main()

