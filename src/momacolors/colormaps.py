from .colors import *
from .plotting import plot_cmaps
from typing import Optional
from matplotlib.colors import Colormap as _Colormap
from matplotlib.colors import LinearSegmentedColormap as _InterpColormap
from matplotlib.colors import ListedColormap as _ListedColormap


def get_colormap(name: str, n: Optional[int]=None, interpolate: bool=False, reversed: bool=False) -> _Colormap:
    """
    Returns a matplotlib colormap object for the specified colormap name.

    Args:
        name (str): The name of the colormap to retrieve.
        n (int, optional): The number of colors to include in the colormap. If not specified,
            the number of colors in the colormap will be used.
        interpolate (bool): Whether to interpolate the colormap to include `n` colors.
            If `True`, the colormap will be interpolated to include `n` colors and the
            default number of colors changes to 256. If `False`, the colormap will be
            truncated or repeated to include `n` colors.
        reversed (bool): Whether to return the reversed colormap. If `True`, the
            reversed colormap will be returned. If `False`, the normal colormap will be returned.

    Returns:
        matplotlib.colors.Colormap: The colormap object for the specified colormap name.

    Raises:
        ValueError: If the specified colormap name is not recognized.

    """
    
    if name.endswith('_r'):
        name = name[:-2]
        reversed = True
    
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

    if reversed:
        return cmap.reversed()
    return cmap


def _compare_names(names: set, subset: set, include_subset: Optional[bool]=None) -> set:
    if include_subset is None:
        return names
    if include_subset:
        return names & subset
    return names - subset


def show_all(n: Optional[int]=None, interpolate: bool=False, reversed: bool=False,
             sequential: Optional[bool]=None, diverging: Optional[bool]=None,
             colorblind_friendly: Optional[bool]=None) -> tuple:
    """
    Displays all colormaps that match the specified criteria.

    Args:
        n: (int, optional). The number of colors to include in each colormap.
            If None, the default number of colors is used.
        interpolate: bool. Whether to interpolate the colormap to include `n` colors.
            If `True`, the colormap will be interpolated to include `n` colors and the
            default number of colors changes to 256. If `False`, the colormap will be
            truncated or repeated to include `n` colors.
        reversed: bool. Whether to reverse the order of colors in the colormap.
        sequential: (bool, optional). Whether to include or exclude sequential colormaps.
            If None, this criteria is ignored.
        diverging: (bool, optional). Whether to include or exclude diverging colormaps.
            If None, this criteria is ignored.
        colorblind_friendly: (bool, optional). Whether to include or exclude colorblind-friendly colormaps.
            If None, this criteria is ignored.

    Returns:
        tuple. A 2-tuple of `matplotlib.Figure` and `matplotlib.Axes` objects.
    
    Raises:
        ValueError: If no colormaps match the specified criteria.
    """
    names = _hex_colors.keys()
    names = _compare_names(names, _sequential, sequential)
    names = _compare_names(names, _diverging, diverging)
    names = _compare_names(names, _colorblind_friendly, colorblind_friendly)
    if len(names) == 0:
        raise ValueError("No colormaps match the specified criteria.")
    cmaps = [get_colormap(name, n=n, interpolate=interpolate, reversed=reversed) for name in sorted(names)]
    return plot_cmaps(cmaps)
