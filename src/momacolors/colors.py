from .hex_colors import _hex_colors
from matplotlib.colors import LinearSegmentedColormap as _InterpColormap
from matplotlib.colors import ListedColormap as _ListedColormap

def colors(name, n=None, interpolate=False):
    reverse = False
    if name.endswith('_r'):
        name = name[:-2]
        reverse = True
    
    if name not in _hex_colors:
        raise ValueError(f"Unknown colormap name {name!r}")

    if interpolate:
        if n is None:
            n = 256
        cmap = _InterpColormap.from_list(name, _hex_colors[name], N=n)
    else:
        if n is None:
            n = len(_hex_colors[name])
        cmap = _ListedColormap(_hex_colors[name], name=name, N=n)

    if reverse:
        return cmap.reversed()
    return cmap
