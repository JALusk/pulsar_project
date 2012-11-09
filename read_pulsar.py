# read_pulsar.py
#
# Routine to read in the data from pulsar3.lis and save the 
# columns as vectors in python

import scipy

def read_pulsar(filename):
  data = scipy.loadtxt(filename, skiprows = 2)
  
  time = data[:,1]
  x = data[:,2]
  y = data[:,3]
  E = data[:,4]
 
  return time, x, y, E
