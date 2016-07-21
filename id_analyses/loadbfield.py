'''
Created on 16 Jun 2016

@author: gdy32713
'''
import h5py
import inspect
import os

def loadBFieldFromHDF5(name):
    path = inspect.stack()[0][1]
    filepath =  '/'.join(os.path.split(path)[0].split(os.sep)[:-2] +
                    ['id_tools/data', name])
    
    f=h5py.File(filepath,'r')
    
    return f

if __name__ == '__main__':
    a = loadBFieldFromHDF5('CPMUplota1ideal.h5')
    
    b = 2+2