#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import plawt

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Three subplots sharing both x/y axes
# f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=False, sharey=True)
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
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0, wspace=0)
plt.savefig('subplottest.png')
plt.close()

plawt.plot({
	0: {'x': x, 'y': y},
	'title': 'Sharing both axes',
	'xlabel': 'Velocity', 'ylabel': 'Amplitude',
	'sharex': True, 'sharey': True,
	'hspace': 0,
	'filename': 'subplotcompare.png'
}, {
	0: {'x': x, 'y': y, 'line': 'bo'}
}, {
	0: {'x': x, 'y': 2*y**2-1, 'line': 'ro'}
})
