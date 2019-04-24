from string import ascii_uppercase
from random import choice


def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a boggle game
    """
    # The function creates a dictionary with the row column tuple as the key and a space as the value
    return {(row, column): choice(ascii_uppercase) 
        for row in range(height)
        for column in range(width)}

        
def neighbours_of_position(coords):
    """
    Get neighbors of a given position
    """
    # Assign a number to a variable
    row = coords[0]
    col = coords[1]
    
    #Assign each of the neighbours
    
    # Top-left to Top-right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # Left to Right
    left = (row, col - 1)
    center = (row, col)
    right = (row, col + 1)
    
    # Bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_right, top_center, top_left,
            left, right,
            bottom_right, bottom_center, bottom_left]

            
def all_grid_neighbours(grid):
    """
    Get all of the possible neighbours for each position in the grid
    """
    
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

    
def path_to_word(grid, path):
    """
    Add all the letters on the path to a string
    """
    # gets the list of letters for the positions in the path and then joins
    # them into a string
    return ''.join([grid[p] for p in path])


def search(grid, dictionary):
    """
    Search throught the paths to locate words by matching
    strings to words in a dictionary
    """
    # First we get the neighbours of
    # every position in the grid and then we get the paths list to capture all paths
    # that form valid words
    
    neighbours = all_grid_neighbours(grid)
   
    # a letter could be repeated
    # in the grid several times if we had two letter A's and we saved a word with an A
    # in it how would we know which A it is
    paths = []
    full_words, stems = dictionary
    
    # The do search function exists within the scope
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

    
# on average a set can say whether it contains a particular
# item or not in constant time. The time taken does not grow as a set grows
# Pre calculating word stems. We know we can check for words starting with the
# current path by linearly searching the dictionary.
# We're going to create a second
# dictionary that contains all of the partial words. We'll call them stems. If
# the dictionary contains the words bus and this, the stems dictionary would
# contain B, BU, T, TH, THI.
def get_dictionary(dictionary_file):
    """
    Load dictionary file
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
                
    return full_words, stems

       
def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))


# Main Function 
def main():
    
    """
    This is the function that will run the whole project
    """
    
    grid = make_grid(3, 3)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    display_words(words)
    
# This line of code to the bottom of boggle.py that execute
# the boggle solver that line of code should only be run when we actually run
# boggle.py from the command line it should be ignored if we're simply
# importing boggle.py into another file. Without this if function, 
# we would not be able to run our unittests as the file boggle.py
# would be imported and fully executed in test_boggle.py.
# Prevents main() running when test_boggle.py is run.


if __name__ == "__main__":
    main()
    