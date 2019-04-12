# Importing Unit Test framework from
# The unit test framework uses classes and inheritance so to create
# tests we will create a class that inherits from the TestCase class in the
# framework and then we write methods inside that class for the actual tests.
import unittest
import boggle 

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
        