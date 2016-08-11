'''
Created on 11 Aug 2016

@author: gdy32713

'''

import numpy as np
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm

def defineMachineProperties(energy = 3.0, c = 2.9911124e8, mass = 0.511e-3):
    const = (0.03/energy)*1e-2
    gamma = energy/mass
    
    return (energy, const, c, mass, gamma)

def fieldPhaseError(BField):
    
    nperiods = len(fm.findPeakIndices(BField))/2
    step = BField[1,0]-BField[0,0]
    n_step = fm.findPeakPeriodicity(BField)
    n_s_stp = len(BField)
    
    
    
    phaseError =1 
    
    return phaseError

