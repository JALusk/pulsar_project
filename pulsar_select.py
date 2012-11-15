# pulsar_select.py
#
# Select events in an aperture about your pulsar's center
# based on coordinates of center, and radius of aperture
#
# Input:
# x0, y0: coordinates of pulsar center
# r: radius of the aperture to use

import math
from read_pulsar import *

# Select points within a certain radius of the center of intensity,
# as defined by the user

def pulsar_select(x0, y0, r):
  pulsar_data = 'pulsar3.lis'
  t, x, y, E = read_pulsar(pulsar_data)
  
  t_signal = []
  x_signal = []
  y_signal = []
  E_signal = []

  for i in range(0, len(x)):
    dist = math.sqrt((x[i] - x0)**2 + (y[i] - y0)**2)
    if dist < r:
      t_signal.append(t[i])
      x_signal.append(x[i])
      y_signal.append(y[i])
      E_signal.append(E[i])
  
  return t_signal, x_signal, y_signal, E_signal
