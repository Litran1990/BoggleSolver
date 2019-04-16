# Importing Unit Test framework from
# The unit test framework uses classes and inheritance so to create
# tests we will create a class that inherits from the TestCase class in the
# framework and then we write methods inside that class for the actual tests.
import unittest
import boggle 
# These are the 26 ASCII uppercase characters A through Z
from string import ascii_uppercase

# Now we fill out the boggle grid with letters

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        # Here the two parameters are height and width
        grid = boggle.make_grid(0, 0)
        # The test assertin is that a grid with 0 height and 0 width has a length of 0
        # The test will fail as we have not yet writte the make_grid method in boogle.py
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        """
        Test to show that all the coordinates
        inside the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        # Here we use the assertIn method to ensure that the (0:0) alongside all possible 
        # coordinates are in a (2:2) grid, whereas the assertNotIn makes sure that
        # the (2:2) coordinate does not belong in a (2:2) grid
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid
        contains uppercase letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    
    def test_neighbors_of_a_position(self):
        """
        In a 3:3 grid, ensures that position has 8 neighbours
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        
        # This is a dictionary where the key is a position
        # just like with the grid itself but the value is a list of neighboring positions
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid) # create a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
            
    def converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1,1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
    def test_search_grid_for_words(self):
        """
        Ensure that certain patterns can be found in a path_to_word
        """
        # So for this test we will create a mock grid so that we can control the letters.
        # In this case it's a 2x2 grid containing the letters a b c and d
        
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
    def test_load_dictionary(self):
        """
        we test that the get_dictionary function returns a dictionary that has a
        length greater than zero
        """
        
        dictionary = boggle.get_dictionary('words.txt')
        self.assertGreater(len(dictionary), 0)