#!/usr/bin/python
from __future__ import division
from math import pi
from numpy import exp, sqrt, log10, e
import numpy as np
import plawt

# excitation potential
def Xn(n): return 13.6*(1-1/n**2)

# Boltzmann equation, N_n/N
def excitationEq(n, T):
	k = 8.63e-5 # eV/K
	gn = 2*n**2; Z = 2 # hydrogen atom
	return (gn/Z) * exp(-Xn(n)/(k*T))

T = np.arange(3000, 12000, 1)
# plt.plot(T, excitationEq(1, T), 'k-', label='Lyman Series $\log{N_1 / N}$')
# plt.plot(T, excitationEq(2, T), 'k--', label='Balmer Series $\log{N_2 / N}$')
# plt.xlabel('Temperature (K)'); plt.ylabel('Relative Population $N_n / N$')
# plt.title('log of Relative Populations of Hydrogen atoms in $n=1$ and $n=2$')
# plt.gca().set_yscale('log'); plt.legend(loc=4); plt.grid()
# plt.ylim((10e-18,10e2)); plt.xlim((2000, 13e3))
# plt.savefig('excitation_logarithmic.png')
# plt.close()

# make sure lines are first, the number doesn't matter so long as its a number
myplot = {
	0: {
		'x': T,
		'y': excitationEq(1, T),
		'line': 'k-',
		'label': 'Lyman Series $\log{N_1 / N}$'
	},
	1:{
		'x': T,
		'y': excitationEq(2, T),
		'line': 'k:',
		'lw': 2.0,
		'label': 'Balmer Series $\log{N_2 / N}$'
	},
	'xlabel': 'Temperature (K)',
	'ylabel': 'Relative Population $N_n / N$',
	'title': 'log of Relative Populations of Hydrogen atoms in $n=1$ and $n=2$',
	'set_yscale': 'log',
	'grid': True,
	'legend': {'loc':4},
	'ylim': (10e-18, 10e2),
	'xlim': (2000,13e3),
	'filename': 'test.png',
	'figsize': (10,5),
	'show': False
}

plawt.plot(myplot)
