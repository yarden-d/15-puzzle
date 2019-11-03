DASH_ROW_FACTOR = 3


def display_board(board_list):
    """
    Print a square board of integers
    :param board_list: A list of integers of length that is a power of 2
    """
    dimension = int(len(board_list)**0.5)
    dash_row = '-' * (dimension * DASH_ROW_FACTOR)
    cur_index = 0
    print(dash_row)
    for i in range(dimension):
        row = '|'
        for j in range(dimension):
            val = str(board_list[cur_index])
            if val == '0':
                val = 'x'
            val += ' ' * (len(str(len(board_list))) - len(val))
            row += val + '|'
            cur_index += 1
        print(row)
        print(dash_row)


def display_message(message):
    print(message)

