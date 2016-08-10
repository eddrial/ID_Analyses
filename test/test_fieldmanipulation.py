'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm


class Test(unittest.TestCase):
    
    testfile = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')


    def testBzValuesGreaterThanBxValues(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        Bxmax = fm.maxOfData(data['Bx'][:])
        self.assertGreater(Bzmax, Bxmax)
        
    def testBzValuesGreaterThanBsValues(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        Bsmax = fm.maxOfData(data['Bs'][:])
        self.assertGreater(Bzmax, Bsmax)
        
    
    def testMaxValueCorrect(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        self.assertGreater(Bzmax, 1.23)
        
    def testNumberOfPeaksInTest(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        numberOfPeaks = len(fm.findPeakIndices(f['Bz'][:]))
        self.assertEqual(numberOfPeaks, 16)
        
    def testPeakPeriodicity(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        peakPeriodicity = fm.findPeakPeriodicity(f['Bz'][:])
        self.assertEqual(peakPeriodicity, 20)
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()