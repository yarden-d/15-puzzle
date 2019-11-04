import random
import math

EMPTY_VALUE = 0


class Board:
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.board = None

    def get_board(self):
        return self.board

    def start(self):
        """
        Fill self.board with a random list of integers
        """
        board = [x for x in range(1, self.dimension**2)]
        board.append(EMPTY_VALUE)
        while self.in_order(board) or not self.is_solvable(board):
            random.shuffle(board)
        self.board = board

    def in_order(self, board=None):
        """
        Check if the list given is in ascending order and the values match the indexes
        :param board: list of integers
        :return: Trues/False
        """
        if not board:
            if self.board:
                board = self.board
            else:
                return False
        for i in range(1, len(board)):
            if i != board[i-1]:
                return False
        return True

    def move(self, value):
        """
        Switch the places between 'value' and '0' in the board
        :param value: An integer in self.board
        :return: self.board after the move
        """
        if value not in self.board:
            return self.board
        index = self.board.index(value)
        neighbours = self._get_neighbours(value)

        if EMPTY_VALUE in neighbours.values():
            empty_index = self.board.index(EMPTY_VALUE)
            self.board[empty_index] = value
            self.board[index] = EMPTY_VALUE
        return self.board

    def _get_neighbours(self, value):
        """
        Returns the values of the 4 neighbours (if they exist) of value in self.board
        :param value: Integer in self.board
        :return: Dictionary with values of neighbours
        """
        neighbours = {
            'above': None,
            'below': None,
            'right': None,
            'left': None
        }
        try:
            index = self.board.index(value)
        except ValueError:
            return neighbours

        neighbours['above'] = self._get_above_neighbour(index)
        neighbours['below'] = self._get_below_neighbour(index)
        neighbours['right'] = self._get_right_neighbour(index)
        neighbours['left'] = self._get_left_neighbour(index)

        return neighbours

    def _get_above_neighbour(self, index):
        neighbour = None
        above_neighbour_index = index - self.dimension
        if above_neighbour_index >= 0:
            neighbour = self.board[above_neighbour_index]
        return neighbour

    def _get_below_neighbour(self, index):
        neighbour = None
        below_neighbour_index = index + self.dimension
        if below_neighbour_index < len(self.board):
            neighbour = self.board[below_neighbour_index]
        return neighbour

    def _get_right_neighbour(self, index):
        neighbour = None
        right_neighbour_index = index + 1
        if right_neighbour_index % self.dimension != 0:
            neighbour = self.board[right_neighbour_index]
        return neighbour

    def _get_left_neighbour(self, index):
        neighbour = None
        left_neighbour_index = index - 1
        if index % self.dimension != 0:
            neighbour = self.board[left_neighbour_index]
        return neighbour

    def is_solvable(self, board):
        if not board:
            board = self.board
        inversions = self.inversions(board)
        row_index = self._get_row_with_empty_value(board)

        if (self.dimension % 2 != 0) and (inversions % 2 == 0):
            return True
        if self.dimension % 2 == 0:
            if (row_index % 2 != 0) and (inversions % 2 != 0):
                return True
            if (row_index % 2 == 0) and (inversions % 2 == 0):
                return True
        return False

    def inversions(self, board):
        """
        Count the number of inversions in the board i.e. the umber of tiles that precede a tile with a smaller value
        :param board: 
        :return: number of inversions 
        """
        if not board:
            board = self.board
        count = 0
        for i in board:
            for j in board[i+1:]:
                if i == 0 or j == 0:
                    continue
                if i > j:
                    count += 1
        return count

    def _get_row_with_empty_value(self, board):
        if not board:
            board = self.board
        index = board.index(EMPTY_VALUE)
        row_number = math.ceil(index/self.dimension)
        return row_number
