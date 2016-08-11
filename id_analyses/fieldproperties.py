'''
Created on 11 Aug 2016

@author: gdy32713
'''

def defineMachineProperties(energy = 3.0, c = 2.9911124e8, mass = 0.511e-3):
    const = (0.03/energy)*1e-2
    gamma = energy/mass
    
    return (energy, const, c, mass, gamma)

