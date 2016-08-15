'''
Created on 11 Aug 2016

@author: gdy32713

'''

import numpy as np
import scipy.signal as signal
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm
import matplotlib.pyplot as plt

def defineMachineProperties(energy = 3.0, c = 2.9911124e8, mass = 0.511e-3):
    const = (0.03/energy)*1e-2
    gamma = energy/mass
    
    return (energy, const, c, mass, gamma)


def fieldPhaseError(BField):
    (energy,const,c,mass,gamma) = defineMachineProperties()
    
    nperiods = len(fm.findPeakIndices(BField[:,2]))
    step = BField[1,0]-BField[0,0]
    n_step = fm.findPeakPeriodicity(BField[:,2])
    n_s_stp = len(BField)
    
    nskip=8
    
    trap_b_array = np.roll(BField[:,1:3], 1, 0)
    trap_b_array[0,:]=0.0
    trap_b_array = (trap_b_array+BField[:,1:3])*step/2
    
    trajectories = np.zeros([n_s_stp,4]) 
    
    trajectories[:,2]=-np.cumsum(np.multiply(const,trap_b_array[:,1]))
    trajectories[:,3]=np.cumsum(np.multiply(const,trap_b_array[:,0]))
    
    trap_traj = np.roll(trajectories, 1, 0)
    trap_traj[0,:]=0.0
    trap_traj=(trap_traj+trajectories)*step/2
    
    trajectories[:,0]=np.cumsum(trap_traj[:,2])
    trajectories[:,1]=np.cumsum(trap_traj[:,3])
    
    #wx=np.cumsum(np.square(trajectories[:,2])*1e-3)
    #wz=np.cumsum(np.square(trajectories[:,3])*1e-3)
    
    detrended_trajectories=signal.detrend(trajectories[:,:],axis=0)
    a=np.gradient(detrended_trajectories[:,0])
    b=np.gradient(detrended_trajectories[:,1])
    w=np.vstack((a,b))
    w=np.square(np.transpose(w))
    
    trap_w = np.roll(w,1,0)
    trap_w[0,:] = 0.0
    trap_w= (trap_w+w)*1e-3*1/2
    
    ph=np.cumsum(trap_w[:,0]+trap_w[:,1])/(2.0*c)

    ph2=(1*1e-3/(2.0*c*gamma**2))*np.arange(n_s_stp)+ph
    
    
    v1=(n_step/2)*np.arange(2*nperiods-1*nskip)+n_s_stp/2-nperiods*n_step/2+(nskip-1)*n_step/4
    v2=ph2[v1[0]:v1[-1]+n_step/2:n_step/2]
            
            
    #'linear fit'
    A=np.vstack([v1,np.ones(len(v1))]).T
    
    m,intercept=np.linalg.lstsq(A, v2)[0]
    Omega0=2*np.pi/(m*n_step)
    
    v2=ph[v1[0]:v1[-1]+n_step/2:n_step/2]
    
        
    #'fit function'
    A=np.vstack([v1,np.ones(len(v1))]).T
    
    m,intercept=np.linalg.lstsq(A, v2)[0]

    phfit=intercept+m*v1
    
    
    ph=v2-phfit
    pherr=np.sum(ph**2)*Omega0**2
    pherrnew=ph*Omega0*360.0/(2.0*np.pi)
    
    pherr=np.sqrt(pherr/(4*nperiods+1-2*nskip))*360.0/(2.0*np.pi)
    
    
    return (pherr, trajectories)



