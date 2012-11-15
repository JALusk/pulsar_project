# pulsar_period.py
#
# Determine the period of the pulsar, make periodogram and phase-binned
# plots of the pulse profile and energy profile

from pylab import *
from pulsar_select import *

# Coordinates of pulsar center, and radius of aperture
x0 = 26415.
y0 = 27684.
r = 150.3

# Read in pulsar signal within the aperture
t, x, y, E = pulsar_select(x0, y0, r)

# Brute-force method - bin the data into 1024 bins
t_hist = histogram(t, bins = 4096)
counts = t_hist[0]
bins = t_hist[1]

# Each bin is a period of time, figure out what that period of time is
time_per_bin = (max(t) - min(t)) / 1024.

# Compute FFT of the counts
Y = fft(counts)
n = len(Y)
power = abs(Y[1:(n/2)])**2
nyquist = 1./2
freq = scipy.array(range(n/2))/(n/2.0)*nyquist
period = 1./freq


# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
pgram = ax.plot(period[1:len(period)],power)
ax.set_title('Pulsar 3 Periodogram')
show()
fig.savefig('pgram')

