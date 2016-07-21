'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
from id_analyses import loadbfield as lb

class Test(unittest.TestCase):


    def testIsHDF5File(self):
        f = lb.loadBFieldFromHDF5()
        self.assertEqual(None, f, "File is not of the correct Type")
        #self.assertEqual('<HDF5 object reference>',f.ref,"File is not of the correct Type")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIsHDF5File']
    unittest.main()