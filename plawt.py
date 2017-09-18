import matplotlib.pyplot as plt
from numpy import ndarray

def plot(*plotStructs):
	if len(plotStructs) == 0:
		raise TypeError("Missing 1 required argument")

	globalParams = plotStructs[0] # set all global properties using the first plotStruct

	# setup subplots
	sharex = globalParams['sharex'] if 'sharex' in globalParams else False
	sharey = globalParams['sharey'] if 'sharey' in globalParams else False

	# setup figure and adjustments
	# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots_adjust
	hspace = globalParams['hspace'] if 'hspace' in globalParams else 0.2
	wspace = globalParams['wspace'] if 'wspace' in globalParams else 0.2
	title  = globalParams['title']  if 'title'  in globalParams else ''

	fig, axes = plt.subplots(len(plotStructs), sharex=sharex, sharey=sharey)
	fig.set_size_inches(globalParams['figsize']) if 'figsize' in globalParams else None
	fig.subplots_adjust(hspace=hspace, wspace=wspace)
	fig.suptitle(title)

	# hack for common x and y labels on subplots
	if sharex or sharey:
		fig.add_subplot(111, frameon=False)
		plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')

		xlabel = globalParams['xlabel']  if 'xlabel' in globalParams else ''
		ylabel = globalParams['ylabel']  if 'ylabel' in globalParams else ''
		plt.xlabel(xlabel) if sharex else None
		plt.ylabel(ylabel) if sharey else None

	if not isinstance(axes, ndarray):
		axes = (axes,) # this makes axes iterable even if there's just one axes

	for i, ax in enumerate(axes):
		plotStruct = plotStructs[i]
		for key in plotStruct:
			val = plotStruct[key]
			if type(key) == int: # its a line
				x          = val['x']
				y          = val['y']          if 'y' in val else None
				linestyle  = val['line']       if 'line' in val else ''
				drawstyle  = val['draw']       if 'draw' in val else 'default'
				label      = val['label']      if 'label' in val else ''
				markersize = val['markersize'] if 'markersize' in val else 6.0
				markersize = val['ms']         if 'ms' in val else markersize
				linewidth  = val['linewidth']  if 'linewidth' in val else 1.0
				linewidth  = val['lw']         if 'lw' in val else linewidth
				alpha      = val['alpha']      if 'alpha' in val else 1.0


				if y is not None:
					line, = ax.plot(x, y, linestyle, drawstyle=drawstyle)
				else:
					line, = ax.plot(y, linestyle, drawstyle=drawstyle)
				mfc = val['markerfacecolor'] if 'markerfacecolor' in val else line.get_markerfacecolor()
				mfc = val['mfc'] if 'mfc' in val else line.get_markerfacecolor()

				line.set_label(label)
				line.set_markersize(markersize)
				line.set_linewidth(linewidth)
				line.set_alpha(alpha)
				line.set_markerfacecolor(mfc)

			elif type(key) == str: # its a property
				ax.set_xlabel(val) if key == 'xlabel' and not sharex else None
				ax.set_ylabel(val) if key == 'ylabel' and not sharey else None
				ax.set_yscale(val) if key == 'set_yscale' else None
				ax.set_xscale(val) if key == 'set_xscale' else None
				ax.grid()          if key == 'grid' and val else None
				ax.set_xlim(val)   if key == 'xlim' else None
				ax.set_ylim(val)   if key == 'ylim' else None
				ax.set_aspect(val) if key == 'aspect' else None

				if key == 'legend':
					legend = val
					loc = legend['loc'] if 'loc' in legend else '1'
					ax.legend(loc=loc)

	# Storing and cleanup of plot
	fig.savefig(globalParams['filename']) if 'filename' in globalParams else None
	plt.show() if 'show' in globalParams and globalParams['show'] else None
	plt.close(fig) if 'keepOpen' not in globalParams or not globalParams['keepOpen'] else None

	return fig # in case people wanna do extra things
