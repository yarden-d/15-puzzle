import graphics
from board import Board
from input import get_move_int

WELCOME_MESSAGE = "Welcome to 15 puzzle"
EXIT_MESSAGE = "WooHoo Genius!"


def main():
    board = Board()
    board.start()
    graphics.display_message(WELCOME_MESSAGE)
    graphics.display_board(board.get_board())

    while not board.in_order():
        move_val = get_move_int()
        board_list = board.move(move_val)
        graphics.display_board(board_list)

    graphics.display_message(EXIT_MESSAGE)


if __name__ == '__main__':
    main()
