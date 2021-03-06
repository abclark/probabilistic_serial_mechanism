"""
=======================================
probabilistic_serial_mechanism.py
=======================================
Runs the probabilistic serial mechanism, taking as input a dictionary R. 
A key of this dictionary corresponds to an agent,
a value the agent's rank order list of the objects. 
Output is a dictionary P. 

A value of the output dictionary is a list whose entries are probabilities that the agent wins the 
corresponding objects.
E.g. for the dictionary R = {0: [0,1,2], 1: [2,1,0]}, there are two agents and three objects. 
Agent 1 ranks object 2 above object 1 above object 0. 
Output for this dictionary is P = {0: array([ 1. ,  0.5,  0. ]), 1: array([ 0. ,  0.5,  1. ])}. 
Agent 0 wins object 0 with probability 1 and object 1 with probability 0.5.

Copyright 2017 Aubrey Clark.

probabilistic_serial_mechanism.py is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.
"""

#: The current version of this package.
__version__ = '0.0.1-dev1'

import numpy as np

def probabilistic_mechanism(R):
  m = np.ones(len(R[0]))
  P={}
  for key, value in R.items():
    P[key]=np.zeros(len(value))
  while max(m) > 0:
    for key,value in R.items():
      R[key] = [i for i in value if m[i] != 0]
    y = np.zeros(len(m))
    for key,value in R.items():
      y[value[0]] += 1
    #time taken to deplete remaining masses
    z = [max(i,0.000001)/max(j,0.0000001) for i,j in zip(m,y)]
    #reduce and allocate masses
    for key,value in R.items():
      m[value[0]] -= min(z)
      P[key][value[0]] += min(z)  
  else:
    return(P)
 
