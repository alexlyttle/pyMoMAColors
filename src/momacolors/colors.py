import numpy as np
from .palettes import palettes
from .plotting import plot_cmaps
from typing import Optional
from matplotlib.colors import ListedColormap


def _check_reversed(name, direction):
    if name.endswith("_r"):
        return name[:-2], -1
    return name, direction


def get_colors(name: str, n: Optional[int]=None, brew_type: Optional[str]=None, direction: int=1,
               override_order: bool=False, return_hex: bool=False) -> np.ndarray:
    name, direction = _check_reversed(name, direction)
    return palettes[name].get_colors(n=n, brew_type=brew_type, direction=direction, override_order=override_order, return_hex=return_hex)


def get_colormap(name: str, n: Optional[int]=None, brew_type: Optional[str]=None, direction: int=1,
                 override_order: bool=False) -> ListedColormap:
    name, direction = _check_reversed(name, direction)
    return palettes[name].get_colormap(n=n, brew_type=brew_type, direction=direction, override_order=override_order)


def show_all(n: Optional[int]=None, brew_type: Optional[str]=None, direction: int=1, override_order: bool=False,
             colorblind_friendly: Optional[bool]=None, sequential: Optional[bool]=None,
             diverging: Optional[bool]=None) -> tuple:
    """
    Displays all colormaps that match the specified criteria.

    Args:
        n (Optional[int]): The number of colors in each colormap. If None, the default number is used.
        brew_type (Optional[str]): The type of colorbrewer palette to use. If None, all types are used.
        direction (int): The direction of the colormap. 1 for forward, -1 for reverse.
        override_order (bool): Whether to override the default order of colors in the colormap.
        colorblind_friendly (Optional[bool]): Whether to use only colorblind-friendly colormaps. If None, all colormaps are used.
        sequential (Optional[bool]): Whether to use only sequential colormaps. If None, all colormaps are used.
        diverging (Optional[bool]): Whether to use only diverging colormaps. If None, all colormaps are used.

    Returns:
        tuple: A 2-tuple of `matplotlib.Figure` and `matplotlib.Axes` objects.
    
    Raises:
        ValueError: If no colormaps match the specified criteria.
    """
    cmaps = []
    for palette in palettes.values():
        if colorblind_friendly is not palette.colorblind_friendly and colorblind_friendly is not None:
            continue
        if sequential is not palette.sequential and sequential is not None:
            continue
        if diverging is not palette.diverging and diverging is not None:
            continue
        cmaps.append(palette.get_colormap(n=n, brew_type=brew_type, direction=direction, override_order=override_order))

    if len(cmaps) == 0:
        raise ValueError("No colormaps match the specified criteria.")
    return plot_cmaps(cmaps)
