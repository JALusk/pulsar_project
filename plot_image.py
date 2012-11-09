# plot_image.py
#
# Plot the x,y coordinates of each detected X-ray in the pulsar data file

from pylab import *
from read_pulsar import *

pulsar_data = 'pulsar3.lis'

# read_pulsar returns time (t), x, y, and energy (E) as vectors
t, x, y, E = read_pulsar(pulsar_data)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, ',')
ax.set_title('X-ray image data, Pulsar 3')
plt.show()
