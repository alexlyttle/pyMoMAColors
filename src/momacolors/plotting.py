import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_cmap(cmap: ListedColormap, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(6.4, 0.72))
    x = np.linspace(0, 1, cmap.N)[None, :]
    ax.imshow(x, aspect='auto', cmap=cmap)
    ax.set_axis_off()
    return ax

def plot_cmaps(cmaps: list):
    """Plot colormaps in list `cmaps`"""
    nrows = len(cmaps)
    figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)

    for ax, cmap in zip(axs, cmaps):
        ax = plot_cmap(cmap, ax=ax)
        ax.text(-.01, .5, cmap.name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    return fig, axs
