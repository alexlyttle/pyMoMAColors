from .hex_colors import _hex_colors
from .utils import plot_cmaps
from matplotlib.colors import LinearSegmentedColormap

__all__ = [
    "Avedon", 
    "Kippenberger",
    "Picabia"
]

_cmaps = {}
for _name in __all__:
    _cmaps[_name] = LinearSegmentedColormap.from_list(_name, _hex_colors[_name])

locals().update(_cmaps)

def show_cmaps():
    return plot_cmaps("Diverging", _cmaps.values())
