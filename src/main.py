from game import C4Game
from tools import get_input

def print_board():
    pass

def main():

    custom = True

    # Start by configuring the options
    if custom:
        # Initialize game with given parameters
        print("Input board width: ")
        width = get_input(int, "width")
        print("Input board height: ")
        height = get_input(int, "height")
        Game = C4Game(width, height)
    else:
        Game = C4Game()

    # run the game loop
    while True:
        # Try to place

        
        while True:
            try:
                print(f"Player {Game.get_cur_player()} please enter index to place piece")
                idx = get_input(int, "index")
                Game.place(idx)
                break
            except Exception as e:
                print(e)
                continue


if __name__ == "__main__":
    main()