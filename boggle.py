def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a boggle game
    """
    # The function creates a dictionary with the row column tuple as the key and a space as the value
    return {(row, column): ' ' for row in range(height)
        for column in range(width)}