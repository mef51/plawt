#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import plawt
import matplotlib as mpl

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

##### Vanilla Matplotlib #####

# Three subplots sharing both x/y axes
# f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
f.suptitle('Sharing both axes')

# hack to have commone x and y labels
# https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
f.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
plt.xlabel('Velocity')
plt.ylabel('Amplitude')

ax1.plot(x, y)
# ax1.set_title('Sharing both axes')
ax2.scatter(x, y)
ax3.scatter(x, 2 * y ** 2 - 1, color='r')
ax1.set_title('panel a', fontsize=12)
ax2.set_title('panel b', fontsize=12)
ax3.set_title('panel c', fontsize=12)
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0.3, wspace=0)
plt.savefig('subplotcompare.png')
plt.close()

##### Same plot but with plawt #####
subtitledict = {'verticalalignment': 'center'}
plawt.plot({
	0: {'x': x, 'y': y},
	'title': 'Sharing both axes',
	'subtitle': 'panel a',
	'subtitledict': {'verticalalignment': 'center'},
	'fontsize': 12,
	'subloc': 'left',
	'xlabel': 'Velocity', 'ylabel': 'Amplitude',
	'sharex': True, 'sharey': True,
	'hspace': 0.3,
	# 'aspect': 16/9,
	'filename': 'subplottest.png'
}, {
	0: {'x': x, 'y': y, 'line': 'bo'},
	'subtitle': 'panel b',
	'subtitledict': {'verticalalignment': 'center'},
	'fontsize': 12,
	'subloc': 'left'
}, {
	0: {'x': x, 'y': 2*y**2-1, 'line': 'ro'},
	'subtitle': 'panel c',
	'subtitledict': {'verticalalignment': 'center'},
	'fontsize': 12,
	'subloc': 'left'
})

