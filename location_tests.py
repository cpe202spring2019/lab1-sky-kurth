import unittest                                                                 
from location import *                                                          
                                                                                
class TestLab1(unittest.TestCase):                                              
                                                                                
    def test_repr(self):                                                        
        """ Test string representation """                                      
        loc = Location("SLO", 35.3, -120.7)                                     
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")             
                                                                                
    def test_eq(self):                                                          
        """ Test class equality values """                                      
        loc = Location("SLO", 35.3, -120.7)                                     
        loc2 = Location("SD", 32.7157, 117.1611)                                
        loc3 = Location("SLO", 35.3, -120.7)                                    
        self.assertEqual(loc, loc3)                                             
                                                                                
if __name__ == "__main__":                                                      
        unittest.main() 
