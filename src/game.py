class Cell():
    """A cell is an object with a state and coordinte"""
    def __init__(self, h: int, w: int):
        # Default to empty
        self.state: int = 0
        self.h: int = h
        self.w: int = w
        self.coord = self.get_coord()


    def get_state(self) -> int:
        return self.state

    def get_coord(self) -> tuple[int, int]:
        return (self.w, self.h)

    def set_state(self, player_id: int):
        self.state = player_id
        

    def __str__(self):
        rep = " "
        match self.state:
            case 1:
                rep = "X"
            case 2:
                rep = "O"

        return f"[{rep}]"

class Board():
    """A board is an object with a collection of cells in a grid, with width and height"""
    def __init__(self, width: int, height: int):
        self.height: int = height
        self.width: int = width
        self.state: list[list[Cell]] = [[Cell(h, w) for h in range(self.height)] for w in range(self.width)]

    def get_cell(self, w: int, h: int) -> Cell:
        return self.state[w][h]

    def __str__(self) -> str:
        out: str = ""

        for h in range(self.height):
            for w in range(self.width):
                out += str(self.get_cell(w, self.height - 1 - h))
            out += "\n"
        return out


class C4Game():
    """A C4 game contains a Board as well as other game related metadata, helper functions, and restrictions"""
    def __init__(self, width: int = 7, height: int = 6, max_players: int = 2):
        self.current_player: int = 1
        self.board: Board = Board(width, height)

    def place(self, width_idx: int):

        # Check if legal
        if width_idx >= self.board.width:
            raise ValueError(f"Input: '{width_idx}' exceeds board width '{self.board.width}'")

        # Check if column is full
        if len(list(filter(lambda cell: cell.state != 0, self.board.state[width_idx]))) == self.board.height:
            raise ValueError(f"Input: '{width_idx}' would overflow column '{width_idx}'") 
        
        # Place
        for cell in self.board.state[width_idx]:
            if not cell.get_state():
                cell.set_state(self.get_cur_player())
                break

        print(self.board)
        self.current_player = self.current_player % 2 + 1

    def get_cur_player(self) -> int:
        return self.current_player


    def __str__(self) -> str:
        raise NotImplementedError()
        pass