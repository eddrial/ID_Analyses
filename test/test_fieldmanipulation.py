'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm


class Test(unittest.TestCase):


    def testBzValuesGreaterThanBxValues(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        Bzmax = fm.maxOfData(f['Bz'][:])
        Bxmax = fm.maxOfData(f['Bx'][:])
        self.assertGreater(Bzmax, Bxmax)
        
    def testBzValuesGreaterThanBsValues(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        pass
        
    
    def testMaxValueCorrect(self):
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()