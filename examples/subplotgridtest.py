#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import plawt

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
plt.close('all')

f, axarr = plt.subplots(2, 2)
f.suptitle('Matplotlib: Grid of subplots')
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 0].text(0, 0.8, 'Text here', fontsize=8)
axarr[0, 1].plot(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[0, 1].text(0, 0.8, 'Text here')
axarr[0, 1].text(0, -1.0, 'Text here too')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].plot(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')
f.subplots_adjust(hspace=0.3)

plt.savefig('matplotlibsubplotgrid.png')
##########

plawt.plot({
	0: {'x': x, 'y': y},
	'nrows':2, 'ncols': 2,
	'title': 'Plawt: Grid of subplots',
	'subtitle': 'Axis [0,0]',
	'hspace': 0.3,
	'text': {'x':0, 'y':0.8, 's': 'Text here', 'fontsize': 8},
	'filename': 'plawtsubplotgrid.png'
}, {
	0: {'x': x, 'y': y},
	'subtitle': 'Axis [0,1]',
	'text': [{'x':0, 'y':0.8, 's': 'Text here'},
			 {'x':0, 'y':-1.0, 's':'Text here too'}],
}, {
	0: {'x': x, 'y': y**2},
	'subtitle': 'Axis [1,0]'
}, {
	0: {'x': x, 'y': y**2},
	'subtitle': 'Axis [1,1]'
})
