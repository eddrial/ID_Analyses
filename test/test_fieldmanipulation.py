'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
import numpy as np
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm


class Test(unittest.TestCase):
    
    testfile = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
    B_Array = fm.makeDataNumpyArray(testfile)
    
    
    def testHDF5GoesToArray(self, file = testfile):
        B_Array = fm.makeDataNumpyArray(file)
        self.assertEqual(np.shape(B_Array), (801L,4L))
    
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
        
    def testNumberOfPeaksInTest(self, data = testfile):
        numberOfPeaks = len(fm.findPeakIndices(data['Bz'][:]))
        self.assertEqual(numberOfPeaks, 16)
        
    def testPeakPeriodicity(self, data = testfile):
        peakPeriodicity = fm.findPeakPeriodicity(data['Bz'][:])
        self.assertEqual(peakPeriodicity, 20)
        
    def testCopiedDataIsOnePeriod(self, data = B_Array):
        duplicatePeriod = fm.copyOnePeriod(data)
        print duplicatePeriod
        self.assertEqual(len(duplicatePeriod), 20)
         
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()