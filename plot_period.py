# plot_period.py
#
# Determine the period of the pulsar by plotting a periodogram 
# of the signal.
#
# Input:
# x0, y0: coordinates of pulsar center
# r: radius of the aperture to use

import scipy
from pylab import *
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

# I've chosen a center and radius for my pulsar, so call pulsar_select

t, x, y, E = pulsar_select(26276., 27940., 291.3)

# Plot a 1D histogram of the pulsar signal

fig = plt.figure()
ax = fig.add_subplot(111)
hist = ax.hist(t, bins=1024)
ax.set_title('Histogram of pulsar event times')
#cb = colorbar(hist[0])
ax.set_xlabel('time')
ax.set_ylabel('count')
show()
fig.savefig('pulsar_events')
