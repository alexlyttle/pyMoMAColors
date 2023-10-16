from .hex_colors import _hex_colors
from .utils import plot_cmaps
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
    _cmaps[_name] = LinearSegmentedColormap.from_list(_name, _hex_colors[_name])

locals().update(_cmaps)

def show_cmaps():
    return plot_cmaps("Sequential", _cmaps.values())
