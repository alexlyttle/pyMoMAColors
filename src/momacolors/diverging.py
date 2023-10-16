from .colors import colors
from .utils import plot_cmaps
from matplotlib.colors import LinearSegmentedColormap

__all__ = [
    "Avedon", 
    "Kippenberger",
    "Picabia"
]

_cmaps = {}
for _name in __all__:
    _cmaps[_name] = colors(_name, interpolate=True)

locals().update(_cmaps)

def show_cmaps():
    return plot_cmaps("Diverging", _cmaps.values())
