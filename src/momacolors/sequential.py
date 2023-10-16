from .utils import plot_cmaps
from .colors import colors
from matplotlib.colors import LinearSegmentedColormap

__all__ = [
    "Alkalay1",
    "Alkalay2",
    "Althoff",
    "Ernst",
    "Exter",
    "Flash",
]

_cmaps = {}
for _name in __all__:
    _cmaps[_name] = colors(_name, interpolate=True)

locals().update(_cmaps)

def show_cmaps():
    return plot_cmaps("Sequential", _cmaps.values())
