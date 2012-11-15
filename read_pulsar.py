# read_pulsar.py
#
# Routine to read in the data from pulsar3.lis and save the 
# columns as vectors in python. Filter out the bad photons

import scipy

def read_pulsar(filename):
  data = scipy.loadtxt(filename, skiprows = 2)
  
  t = data[:,1]
  x = data[:,2]
  y = data[:,3]
  E = data[:,4]
  flag = data[:,5]

  t_good = []
  x_good = []
  y_good = []
  E_good = []

  # Filter out the bad photons (flag not equal zero)
  # and create lists of good photon data
  for i in range(0, len(t)):
    if flag[i] == 0:
      t_good.append(t[i])
      x_good.append(x[i])
      y_good.append(y[i])
      E_good.append(E[i])
  
  return t_good, x_good, y_good, E_good
