'''
Created on 16 Jun 2016

@author: gdy32713
'''
import h5py

def loadBFieldFromHDF5():
    f=h5py.File('..\Data\CPMUplota1ideal.h5','r')
    
    return f

if __name__ == '__main__':
    a = loadBFieldFromHDF5()
    
    b = 2+2