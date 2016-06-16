'''
Created on 13 Jun 2016

@author: gdy32713
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt




if __name__ == "__main__" :

    f=h5py.File('U:\Mathematica\CPMUhybrid\CPMUplota1ideal.h5','r')
    
    
    s = np.array(f['s'])
    Bxfield = np.array(f['Bx'])
    Bsfield = np.array(f['Bs'])    
    Bzfield = np.array(f['Bz'])
    
    Bfield = np.array([Bxfield, Bsfield, Bzfield])
    print (np.shape(Bfield))

    plt.figure(1)
    line1 = plt.plot(Bzfield)
    plt.show(1)
    
    insx = Bxfield[390:410]
    inss = Bsfield[390:410]
    insz = Bzfield[390:410]
    
    for x in range(98):
        Bxfield = np.insert(Bxfield, 410, insx)
        Bsfield = np.insert(Bsfield, 410, inss)
        Bzfield = np.insert(Bzfield, 410, insz)
    
    
    Bfield = np.array([Bxfield, Bsfield, Bzfield])
    print (np.shape(Bfield))
    
    plt.figure(2)
    line2 = plt.plot(np.transpose(Bfield[0:2,:]))
    plt.show(2)
    
    print len(Bzfield)
    
    step = s[1]-s[0]
    L= len(Bzfield)
    s = np.arange(((-L+1)*step/2),(L*step/2),step)
    print(s[1380:1382])
    print len(s)