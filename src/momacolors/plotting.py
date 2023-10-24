import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from typing import Optional
from math import ceil
from .palettes import Palette

def plot_cmap(cmap: ListedColormap, ax=None):
    if ax is None:
        _, ax = plt.subplots(figsize=(3, 3), tight_layout=True)
    x = np.linspace(0, 1, cmap.N)[None, :]
    ax.imshow(x, aspect='auto', cmap=cmap)
    ax.set_axis_off()
    return ax

def plot_cmaps(cmaps: list, ncols: int=6, figwidth: int=8):
    """Plot colormaps in list `cmaps`"""
    nrows = ceil(len(cmaps) / ncols)
    figsize = (
        figwidth, figwidth * nrows/ncols
    )
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axs = axes.ravel()
    for ax, cmap in zip(axs, cmaps):
        ax = plot_cmap(cmap, ax=ax)
        # ax.set_box_aspect(0.75)
        ax.set_title(cmap.name, fontsize=10)

    remaining = len(cmaps) - nrows*ncols
    if remaining < 0:
        for ax in axs[remaining:]:
            ax.remove()

    fig.tight_layout()
    return fig, axes
