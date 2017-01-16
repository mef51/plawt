#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt


def plot(plotStruct):
	lines = []
	for key in plotStruct:
		val = plotStruct[key]
		if type(key) == int: # its a line
			x = val['x']
			y = val['y']
			line = val['line'] if 'line' in val else ''
			label = val['label'] if 'label' in val else ''
			plt.plot(x, y, line, label=label)
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

	if 'filename' in plotStruct:
		plt.savefig(plotStruct['filename'])
	if 'show' in plotStruct:
		plt.show()
		plt.close()
	return plt # in case people wanna do extra shit
