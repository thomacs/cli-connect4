from game import C4Game
from tools import get_input

def print_board():
    pass

def main():

    custom = True

    # Start by configuring the options
    if custom:
        # Initialize game with given parameters
        print("\033[2J\033[H", end="") # Clear terminal
        width = get_input("Input board width: ", int, "width")
        height = get_input("Input board height: ", int, "height")
        Game = C4Game(width, height)
    else:
        Game = C4Game()

    # run the game loop    
    while True:
        # Try to place
        print("\033[2J\033[H", end="") # Clear terminal
        print("")
    
        while True:
            try:
                print(f"Player {Game.get_cur_player()} please enter index to place piece {Game.get_piece(Game.get_cur_player())}")
                print(Game)
                idx = get_input("Input index to drop: ", int, "index")
                Game.place(idx)
                break
            except Exception as e:
                print("\033[2J\033[H", end="") # Clear terminal
                print(f"\033[91m{e}\033[0m")
                continue

        # Check for win
        won = Game.check()
        if won:
            break

    print(f"Player {won} won!")

if __name__ == "__main__":
    main()