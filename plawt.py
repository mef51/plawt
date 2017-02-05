#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt


def plot(plotStruct):
	lines = []

	# setup
	if 'figsize' in plotStruct:
		plt.figure(figsize=plotStruct['figsize'])

	for key in plotStruct:
		val = plotStruct[key]
		if type(key) == int: # its a line
			x = val['x']
			y = val['y'] if 'y' in val else None
			line = val['line'] if 'line' in val else ''
			label = val['label'] if 'label' in val else ''
			markersize = val['markersize'] if 'markersize' in val else 6.0
			markersize = val['ms'] if 'ms' in val else markersize
			linewidth = val['linewidth'] if 'linewidth' in val else 1.0
			linewidth = val['lw'] if 'lw' in val else linewidth

			if y is None:
				plt.plot(x, line, label=label, ms=markersize, lw=linewidth)
			else:
				plt.plot(x, y, line, label=label, ms=markersize, lw=linewidth)
		elif type(key) == str: # its a property
			if key == 'xlabel':
				plt.xlabel(val)
			if key == 'ylabel':
				plt.ylabel(val)
			if key == 'title':
				plt.title(val)
			if key == 'set_yscale':
				plt.gca().set_yscale(val)
			if key == 'grid':
				plt.grid()
			if key == 'legend':
				legend = val
				loc = legend['loc'] if 'loc' in legend else '1'
				plt.legend(loc=loc)
			if key == 'xlim':
				plt.xlim(val)
			if key == 'ylim':
				plt.ylim(val)

	# Storing and cleanup of plot
	if 'filename' in plotStruct:
		plt.savefig(plotStruct['filename'])
	if 'show' in plotStruct and plotStruct['show']:
		plt.show()
	if 'keepOpen' not in plotStruct or not plotStruct['keepOpen']:
		plt.close()

	return plt # in case people wanna do extra shit
