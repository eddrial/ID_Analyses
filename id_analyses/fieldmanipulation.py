'''
Created on 16 Jun 2016

@author: gdy32713
'''

import h5py
import numpy as np
#import matplotlib.pyplot as plt

def makeDataNumpyArray(testfile):
    combined = np.vstack((np.array(testfile['s'][:]),np.array(testfile['Bx'][:]),np.array(testfile['Bz'][:]),np.array(testfile['Bs'][:])))
    transposed = np.transpose(combined)
    return transposed

def maxOfData(data):
    return max(data)

def findPeakIndices(data):
    return [i for i, x in enumerate(data) if x > 0.97*maxOfData(data)]

def findPeakPeriodicity(data):
    peakIndices = findPeakIndices(data)
    return peakIndices[1]-peakIndices[0]

def copyOnePeriod(data):
    periodicity = findPeakPeriodicity(data[:,2])
    duplicatesection = data[(len(data)-1)/2:((len(data)-1)/2+periodicity)]
    return duplicatesection
    