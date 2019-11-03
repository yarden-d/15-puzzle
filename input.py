
def get_move_int():
    while True:
        index = input("Please type the number you wish to move to 'x': ")
        try:
            index = int(index)
            return index
        except (ValueError, TypeError):
            continue


