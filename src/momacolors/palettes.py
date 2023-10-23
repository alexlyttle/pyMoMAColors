import numpy as np
from typing import Optional
from matplotlib.colors import ListedColormap, to_rgba_array, to_hex


class Palette:
    def __init__(self, name: str, colors: list, order: Optional[list]=None, colorblind_friendly: bool=False, sequential: bool=False, diverging: bool=False):
        self.name = name
        self.colors = colors
        self.num_colors = len(self.colors)
        self.order = list(range(self.num_colors)) if order is None else order
        assert self.num_colors == len(self.order)  # must be same length
        self.colorblind_friendly = colorblind_friendly
        assert not (sequential and diverging)  # can't be both
        self.sequential = sequential
        self.diverging = diverging
    
    def _check_direction(self, direction: int) -> int:
        if direction not in [-1, 1]:
            raise ValueError(f"Direction must be -1 or 1, not {direction!r}")
        return direction

    def brew_discrete(self, n: int, direction: int=1, override_order: bool=False) -> list:
        """Returns a discrete list of colors from the palette.

        Args:
            n (int): The number of colors to return.
            direction (int): The direction to return the colors in. 1 for forward, -1 for reverse. Default is 1.
            override_order (bool): If True, ignores the order of colors in the palette and returns the first n colors.

        Returns:
            list: A list of hex color codes.

        Raises:
            ValueError: If direction is not -1 or 1.
        """
        direction = self._check_direction(direction)
        rounds = n // self.num_colors
        remainder = n % self.num_colors
        colors = []

        for _ in range(rounds):
            colors.extend(self.colors[::direction])

        if override_order or rounds > 0:
            colors.extend(self.colors[::direction][:remainder])
        
        else:
            colors.extend(
                [self.colors[i] for i in range(self.num_colors) if self.order[i] in range(1, remainder + 1)][::direction]
            )

        return colors

    def brew_continuous(self, n: int, direction: int=1) -> list:
        """Returns a continuous list of colors from the palette. Colors in the palette are interpolated linearly.

        Args:
            n (int): The number of colors to return.
            direction (int): The direction to return the colors in. 1 for forward, -1 for reverse. Default is 1.

        Returns:
            list: A list of hex color codes.

        Raises:
            ValueError: If direction is not -1 or 1.
        """
        direction = self._check_direction(direction)
        rgba = to_rgba_array(self.colors)
        x = np.linspace(0, 1, n)
        xp = np.linspace(0, 1, self.num_colors)
        interp = lambda fp: np.interp(x, xp, fp)
        rgba_interp = np.apply_along_axis(interp, 0 , rgba)[::direction]

        return np.apply_along_axis(to_hex, 1, rgba_interp).tolist()

    def get_colors(self, n: Optional[int]=None, brew_type: Optional[str]=None, direction: int=1,
                       override_order: bool=False) -> list:
        """Returns a list of colors from the palette.

        Args:
            n (int, optional): The number of colors to return. If None, returns all colors in the palette. Default is None.
            brew_type (str, optional): The type of color brew to return. If None, returns a continuous brew if n > number of colors,
                otherwise returns a discrete brew. Default is None.
            direction (int): The direction to return the colors in. 1 for forward, -1 for reverse. Default is 1.
            override_order (bool): If True, ignores the order of colors in the palette and returns the first n colors.

        Returns:
            list: A list of hex color codes.

        Raises:
            ValueError: If direction is not -1 or 1, or if an unknown brew type is specified.
        """
        n = self.num_colors if n is None else n

        if brew_type is None:
            brew_type = "continuous" if n > self.num_colors else "discrete"

        if brew_type == "discrete":            
            return self.brew_discrete(n, direction=direction, override_order=override_order)

        elif brew_type == "continuous":
            return self.brew_continuous(n, direction=direction)

        else:
            raise ValueError(f"Unknown brew type {brew_type!r}")            

    def get_colormap(self, n: Optional[int]=None, brew_type: Optional[str]=None, direction: int=1,
                     override_order: bool=False) -> ListedColormap:
        """Returns a matplotlib.ListedColormap from the palette.

        Args:
            n (int, optional): The number of colors to return. If None, returns all colors in the palette. Default is None.
            brew_type (str, optional): The type of color brew to return. If None, returns a continuous brew if n > number of colors,
                otherwise returns a discrete brew. Default is None.
            direction (int): The direction to return the colors in. 1 for forward, -1 for reverse. Default is 1.
            override_order (bool): If True, ignores the order of colors in the palette and returns the first n colors.

        Returns:
            matplotlib.ListedColormap: Colormap.

        Raises:
            ValueError: If direction is not -1 or 1, or if an unknown brew type is specified.
        """
        colors = self.get_colors(n=n, brew_type=brew_type, direction=direction, override_order=override_order)
        name = self.name
        if direction == -1:
            name += "_r"
        return ListedColormap(colors, name)


_palettes = [
    Palette("Abbott", ["#950404", "#e04b28", "#c38961", "#9f5630", "#388f30", "#0f542f", "#007d82", "#004042"], [1, 6, 5, 4, 3, 8, 2, 7]),
    Palette("Alkalay1", ["#241d1d", "#5b2125", "#8d3431", "#bf542e", "#e9a800"], [5, 1, 4, 3, 2], True, True),
    Palette("Alkalay2", ["#ebcf2e", "#b4bf3a", "#88ab38", "#5e9432", "#3b7d31", "#225f2f", "#244422", "#252916"], list(range(1, 9)), True, True),
    Palette("Althoff", ["#ff9898", "#d9636c", "#a91e45", "#691238", "#251714"], [2, 4, 1, 3, 5], True, True),
    Palette("Andri", ["#f56455", "#15134b", "#87c785", "#572f30"], list(range(1, 5)), True),
    Palette("Avedon", ["#ff7200", "#ff8827", "#ff9c4c", "#ffb274", "#f1caa8", "#e3e1dc","#c2ceaa", "#a1ba77", "#8bac54", "#7ea13e", "#648c16"], [10, 1, 8, 4, 6, 3, 7, 5, 9, 2, 11], False, False, True),
    Palette("Budnitz", ["#86dd45", "#f6e71c", "#fda900", "#fd5300", "#57348b"], list(range(1, 6))),
    Palette("Clay", ["#c48329", "#8b3b36", "#a2b4b7", "#514a2e", "#cf9860", "#8E4115"], list(range(1, 7))),
    Palette("Connors", ["#d92a05", "#f35d36", "#fc9073", "#ffba1b", "#60cfa1"], [5, 1, 4, 3, 2], True),
    Palette("Dali", ["#b4b87f", "#9c913f", "#585b33", "#6ea8ab", "#397893", "#31333f", "#8f5715", "#ba9a44", "#cfbb83"], [8, 3, 7, 1, 5, 9, 2, 6, 4]),
    Palette("Doughton", ["#155b51", "#216f63", "#2d8277", "#3a9387", "#45a395", "#c468b2", "#af509c", "#803777", "#5d2155", "#45113f"], [9, 3, 7, 1, 5, 6, 2, 8, 4, 10], True),
    Palette("Ernst", ["#e8e79a", "#c2d89a", "#8cbf9a", "#5fa2a4", "#477b95", "#315b88", "#24396b", "#191f40"], [4, 2, 6, 1, 3, 8, 5, 7], True, True),
    Palette("Exter", ["#ffec9d", "#fac881", "#f4a464", "#e87444", "#d9402a", "#bf2729", "#912534", "#64243e", "#3d1b28", "#161212"], [4, 9, 2, 5, 7, 1, 6, 3, 8, 10], True, True),
    Palette("Flash", ["#e3c0db", "#db95cb", "#cd64b5", "#B83D9F", "#900c7e", "#680369", "#41045a", "#140e3a"], [4, 6, 1, 7, 2, 5, 3, 8], True, True),
    Palette("Fritsch", ["#0f8d7b", "#8942bd", "#1e1a1a", "#eadd17"], [1, 3, 4, 2], True),
    Palette("Kippenberger", ["#8b174d", "#ae2565", "#c1447e", "#d06c9b", "#da9fb8", "#d9d2cc","#adbe7c", "#8ba749", "#6e8537", "#4f5f28", "#343d1f"], [10, 6, 1, 8, 4, 3, 5, 9, 2, 7, 11], True, False, True),
    Palette("Klein", ["#ff4d6f", "#579ea4", "#df7713", "#f9c000", "#86ad34", "#5d7298", "#81b28d", "#7e1a2f", "#2d2651", "#c8350d", "#bd777a"], list(range(1, 12))),
    Palette("Koons", ["#d8537d", "#6DC5B2", "#eeca76", "#5d2314", "#b5282a"], [1, 2, 3, 5, 4], True),
    Palette("Levine1", ["#E0D9B2", "#818053", "#6B3848", "#8B3E50", "#D5BB6C", "#3F3A4B", "#474C66", "#A5806F"], [5, 4, 6, 1, 2, 7, 3, 8]),
    Palette("Levine2", ["#E3C1CB", "#AD5A6B", "#C993A2", "#365C83", "#384351", "#4D8F8B", "#CDD6AD"], [7, 1, 5, 3, 6, 2, 4], True),
    Palette("Liu", ["#9fd7bd", "#9b5c1c", "#97c124", "#3b5f13", "#ddb25d", "#5c4a32"], list(range(1, 7))),
    Palette("Lupi", ["#61bea4", "#b6e7e0", "#aa3f5d", "#daa5ac", "#98a54f", "#2e92a2", "#ffb651", "#d85a44"], [1, 6, 2, 8, 7, 3, 4, 5]),
    Palette("Ohchi", ["#582851", "#40606d", "#69a257", "#e3d19c", "#c4024d"], [3, 4, 1, 2, 5], True),
    Palette("OKeeffe", ["#f3d567", "#ee9b43", "#e74b47", "#b80422", "#172767", "#19798b"], list(range(1, 7)), True),
    Palette("Palermo", ["#1b80ad", "#ea5b57", "#9c5555", "#0c3c5f"], list(range(1, 5)), True),
    Palette("Panton", ["#e84a00", "#bb1d2c", "#9b0c43", "#661f66", "#2c1f62", "#006289", "#004759"], list(range(1, 8))),
    Palette("Picabia", ["#53362e", "#744940", "#9f7064", "#c99582", "#e6bcac", "#e2d8d6", "#a5a6ae","#858794", "#666879", "#515260", "#3d3d47"], [10, 4, 8, 1, 6, 3, 7, 2, 9, 5, 11], True, False, True),
    Palette("Picasso", ["#d5968c", "#c2676d", "#5c363a", "#995041", "#45939c", "#0f6a81"], [6, 3, 4, 2, 1, 5], True),
    Palette("Rattner", ["#de8e69", "#f1be99", "#c1bd38", "#7a9132", "#4c849a", "#184363", "#5d5686", "#a39fc9"], [1, 5, 6, 2, 3, 7, 8, 4], True),
    Palette("Sidhu", ["#af4646", "#762b35", "#005187", "#251c4a", "#78adb7", "#4c9a77", "#1b7975"], [5, 2, 6, 7, 3, 4, 1], True),
    Palette("Smith", ["#ef7923", "#75bca9", "#7b89bb", "#e9de97", "#2a2e38"], list(range(1, 6)), True),
    Palette("ustwo", ["#d7433b", "#f06a63", "#ff8e5e", "#ffcc3d", "#95caa6", "#008d98"], [6, 5, 2, 3, 1, 4], True),
    Palette("VanGogh", ["#c3a016", "#c3d878", "#58a787", "#8ebacd", "#246893", "#163274", "#0C1F4b"], [2, 4, 3, 6, 1, 5, 7], True),
    Palette("vonHeyl", ["#f96149", "#ffa479", "#e7d800", "#94aec2", "#0d0c0b"], [1, 4, 2, 3, 5], True),
    Palette("Warhol", ["#ff0066", "#328c97", "#d1aac2", "#a5506d", "#b3e0bf", "#2A9D3D", "#edf181", "#db7003", "#fba600", "#f8c1a6", "#A30000", "#ff3200", "#011a51", "#97d1d9", "#916c37"], list(range(1, 16)))
]

palettes = {palette.name: palette for palette in _palettes}
