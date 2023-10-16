import numpy as np
import matplotlib.pyplot as plt

def plot_cmaps(cmap_category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)

    axs[0].set_title(f"{cmap_category} colormaps", fontsize=14)

    for ax, cmap in zip(axs, cmap_list):
        x = np.linspace(0, 1, cmap.N)[None, :]
        ax.imshow(x, aspect='auto', cmap=cmap)
        ax.text(-.01, .5, cmap.name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)
        ax.set_axis_off()
        
    return fig, axs
