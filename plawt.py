#!/usr/bin/python3
from __future__ import division
import matplotlib.pyplot as plt

def plot(plotStruct):
	lines = []

	# setup
	fig, ax = plt.subplots()
	fig.set_size_inches(plotStruct['figsize']) if 'figsize' in plotStruct else None

	for key in plotStruct:
		val = plotStruct[key]
		if type(key) == int: # its a line
			x          = val['x']
			y          = val['y']          if 'y' in val else None
			linestyle  = val['line']       if 'line' in val else None
			label      = val['label']      if 'label' in val else ''
			markersize = val['markersize'] if 'markersize' in val else 6.0
			markersize = val['ms']         if 'ms' in val else markersize
			linewidth  = val['linewidth']  if 'linewidth' in val else 1.0
			linewidth  = val['lw']         if 'lw' in val else linewidth
			alpha      = val['alpha']      if 'alpha' in val else 1.0

			line, = ax.plot(x, y, linestyle) if y is not None else ax.plot(y, linestyle)
			mfc = val['markerfacecolor'] if 'markerfacecolor' in val else line.get_markerfacecolor()
			mfc = val['mfc'] if 'mfc' in val else line.get_markerfacecolor()

			line.set_label(label)
			line.set_markersize(markersize)
			line.set_linewidth(linewidth)
			line.set_alpha(alpha)
			line.set_markerfacecolor(mfc)

		elif type(key) == str: # its a property
			ax.set_xlabel(val) if key == 'xlabel' else None
			ax.set_ylabel(val) if key == 'ylabel' else None
			ax.set_title(val)  if key == 'title' else None
			ax.set_yscale(val) if key == 'set_yscale' else None
			ax.set_xscale(val) if key == 'set_xscale' else None
			ax.grid()          if key == 'grid' and val else None
			ax.set_xlim(val)   if key == 'xlim' else None
			ax.set_ylim(val)   if key == 'ylim' else None

			if key == 'legend':
				legend = val
				loc = legend['loc'] if 'loc' in legend else '1'
				ax.legend(loc=loc)

	# Storing and cleanup of plot
	fig.savefig(plotStruct['filename']) if 'filename' in plotStruct else None
	plt.show() if 'show' in plotStruct and plotStruct['show'] else None
	plt.close(fig) if 'keepOpen' not in plotStruct or not plotStruct['keepOpen'] else None


	return fig # in case people wanna do extra things
