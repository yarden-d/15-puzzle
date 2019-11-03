import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_start(self):
        self.assertFalse(self.board.in_order())
        self.assertIsNone(self.board.get_board())
        self.board.start()
        self.assertIsNotNone(self.board.get_board())
        self.assertFalse(self.board.in_order())
        self.assertEqual(self.board.dimension**2, len(self.board.get_board()))
        for i in range(self.board.dimension**2):
            self.assertTrue(i in self.board.get_board())

    def test_in_order(self):
        scrambled_board = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        ordered_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        self.assertIsNone(self.board.get_board())
        self.assertFalse(self.board.in_order())

        self.board.board = scrambled_board
        self.assertFalse(self.board.in_order())
        self.board.board = ordered_board
        self.assertTrue(self.board.in_order())

    def test_move(self):
        original_board = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        left_move_board = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        up_move_board = [1, 0, 3, 4, 5, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.board.board = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        empty_index = self.board.get_board().index(0)

        # move right/left
        left_neighbour = self.board._get_left_neighbour(empty_index)
        self.board.move(left_neighbour)
        self.assertEqual(self.board.get_board(), left_move_board)
        self.board.move(left_neighbour)
        self.assertEqual(self.board.get_board(), original_board)

        # move up/down
        above_neighbour = self.board._get_above_neighbour(empty_index)
        self.board.move(above_neighbour)
        self.assertEqual(self.board.get_board(), up_move_board)
        self.board.move(above_neighbour)
        self.assertEqual(self.board.get_board(), original_board)

        # no move
        not_a_neighbour = 15
        self.board.move(not_a_neighbour)
        self.assertEqual(self.board.get_board(), original_board)
