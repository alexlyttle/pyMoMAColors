from .hex_colors import _hex_colors
from .utils import plot_cmaps
from matplotlib.colors import ListedColormap

__all__ = [
    "Abbott",  
    "Andri",      
    "Budnitz",    
    "Clay",       
    "Connors",    
    "Dali",       
    "Doughton",        
    "Fritsch",    
    "Klein",       
    "Koons",      
    "Levine1",    
    "Levine2",    
    "Liu",        
    "Lupi",       
    "Ohchi",      
    "OKeeffe",    
    "Palermo",    
    "Panton",     
    "Picasso",    
    "Rattner",    
    "Sidhu",    
    "Smith",      
    "ustwo",      
    "VanGogh",    
    "vonHeyl",    
    "Warhol",      
]

_cmaps = {}
for _name in __all__:
    _cmaps[_name] = ListedColormap(_hex_colors[_name], _name)

locals().update(_cmaps)

def show_cmaps():
    return plot_cmaps("Qualitative", _cmaps.values())
