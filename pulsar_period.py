# pulsar_period.py
#
# Determine the period of the pulsar, make periodogram and phase-binned
# plots of the pulse profile and energy profile

from pylab import *
from pulsar_select import *

# Coordinates of pulsar center, and radius of aperture
x0 = 26276.
y0 = 27943.
r = 150.0

# Read in pulsar signal within the aperture
t, x, y, E = pulsar_select(x0, y0, r)

# Making the time a little easier to understand by switching to 
# relative time from the first observed event
t_rel = t - min(t)

# Making bins of 1/100 second
obs_time = max(t_rel)
Nbins = math.ceil(obs_time)*1000.

# Bin the time data in 1/100 second bins
t_hist = histogram(t_rel, bins = Nbins, range=(0, math.ceil(obs_time)))
counts = t_hist[0]
bins = t_hist[1]

# Compute FFT of the counts
Y = fft(counts)
n = len(Y)
power = abs(Y[1:(n-1)/2])**2
F = fftfreq(n)
period = 1./F

# Find the period corresponding to the max of the power
pulsar_period = period[argmax(power)]/1000.
print 'Pulsar period =', pulsar_period, '(s)'

# Plot figure
#fig = plt.figure()
#ax = fig.add_subplot(111)
#pgram = ax.plot(period[1:len(power)+1]/500.,power)
#ax.set_xscale('log')
#ax.set_xlim([1.0E-2, 1.0E0])
#ax.set_title('Pulsar 3 Periodogram')
#show()
#fig.savefig('pgram')

phase1 = []
phase2 = []

# Create an array of the photon phase
# Trying to bin it so I can plot two periods
for j in range(len(t_rel)):
  int_number_of_periods = modf(t_rel[j] / pulsar_period)[1]
  dec_number_of_periods = modf(t_rel[j] / pulsar_period)[0]
  if int_number_of_periods % 2 == 0: # point belongs in first period
    phase1.append(dec_number_of_periods)
  else: # point belongs in second period
    phase2.append(1.0 + dec_number_of_periods)

# Plot histogram of the phase
fig = plt.figure()
ax = fig.add_subplot(111)
phasehist = ax.hist(phase1 + phase2, bins = 100)
ax.set_title('Pulsar 3: Two Phase Plot')
show()
fig.savefig('phaseplot')
