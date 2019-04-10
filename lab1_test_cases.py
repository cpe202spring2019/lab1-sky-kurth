aimport unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """ Confirms Error is raised when list is none """
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """ Confirms function returns max value in int list """
        self.assertEqual(max_list_iter([5, 3, 8, 9, 3]), 9)
        """ Confirms None is returned for empty lists """
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        """Confirms Error is raised when list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            test_reverse_rec(tlist)
        """ Confirms function returns reversed int list """
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        """ Confirms Error is raised when list is none """
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            test_bin_search(tlist)
    
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        """ Confirms bin search returns correct index """
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        """ Confirms bin search returns correct index if index original high """
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        """ Confirms bin search returns None for invalid target """
        self.assertEqual(bin_search(80, 0, len(list_val)-1, list_val), None )

if __name__ == "__main__":
        unittest.main()

    
