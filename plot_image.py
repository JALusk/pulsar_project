# plot_image.py
#
# Plot the x,y coordinates of each detected X-ray in the pulsar data file

from pylab import *
from read_pulsar import *
from pulsar_select import *

pulsar_data = 'pulsar3.lis'

# read_pulsar returns time (t), x, y, and energy (E) as vectors
t, x, y, E = read_pulsar(pulsar_data)
# Alternately, just plot the selected points
#x0 = 26276.
#y0 = 27943.
#r = 150.0

#t, x, y, E = pulsar_select(x0, y0, r)

fig = plt.figure()
ax = fig.add_subplot(111)
hist = ax.hist2d(x,y,bins=512,cmap=cm.hot_r)
ax.set_title('X-ray image data, Pulsar 3: binned 512x512')
#cb = colorbar(hist[0])
#cb.set_label('counts')
show()
fig.savefig('hist')
