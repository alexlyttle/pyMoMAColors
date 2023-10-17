__all__ = [
    "_hex_colors",
    "_sequential",
    "_diverging",
    "_colorblind_friendly"
]

_hex_colors = {
    "Abbott"      : ["#950404", "#e04b28", "#c38961", "#9f5630", "#388f30", "#0f542f", "#007d82", "#004042"],
    "Alkalay1"    : ["#241d1d", "#5b2125", "#8d3431", "#bf542e", "#e9a800"],
    "Alkalay2"    : ["#ebcf2e", "#b4bf3a", "#88ab38", "#5e9432", "#3b7d31", "#225f2f", "#244422", "#252916"],
    "Althoff"     : ["#ff9898", "#d9636c", "#a91e45", "#691238", "#251714"],
    "Andri"       : ["#f56455", "#15134b", "#87c785", "#572f30"],
    "Avedon"      : ["#ff7200", "#ff8827", "#ff9c4c", "#ffb274", "#f1caa8", "#e3e1dc","#c2ceaa", "#a1ba77", "#8bac54", "#7ea13e", "#648c16"],
    "Budnitz"     : ["#86dd45", "#f6e71c", "#fda900", "#fd5300", "#57348b"],
    "Clay"        : ["#c48329", "#8b3b36", "#a2b4b7", "#514a2e", "#cf9860", "#8E4115"],
    "Connors"     : ["#d92a05", "#f35d36", "#fc9073", "#ffba1b", "#60cfa1"],
    "Dali"        : ["#b4b87f", "#9c913f", "#585b33", "#6ea8ab", "#397893", "#31333f", "#8f5715", "#ba9a44", "#cfbb83"],
    "Doughton"    : ["#155b51", "#216f63", "#2d8277", "#3a9387", "#45a395", "#c468b2", "#af509c", "#803777", "#5d2155", "#45113f"],
    "Ernst"       : ["#e8e79a", "#c2d89a", "#8cbf9a", "#5fa2a4", "#477b95", "#315b88", "#24396b", "#191f40"],
    "Exter"       : ["#ffec9d", "#fac881", "#f4a464", "#e87444", "#d9402a", "#bf2729", "#912534", "#64243e", "#3d1b28", "#161212"],
    "Flash"       : ["#e3c0db", "#db95cb", "#cd64b5", "#B83D9F", "#900c7e", "#680369", "#41045a", "#140e3a"],
    "Fritsch"     : ["#0f8d7b", "#8942bd", "#1e1a1a", "#eadd17"],
    "Kippenberger": ["#8b174d", "#ae2565", "#c1447e", "#d06c9b", "#da9fb8", "#d9d2cc","#adbe7c", "#8ba749", "#6e8537", "#4f5f28", "#343d1f"],
    "Klein"       : ["#ff4d6f", "#579ea4", "#df7713", "#f9c000", "#86ad34", "#5d7298", "#81b28d", "#7e1a2f", "#2d2651", "#c8350d", "#bd777a"],
    "Koons"       : ["#d8537d", "#6DC5B2", "#eeca76", "#5d2314", "#b5282a"],
    "Levine1"     : ["#E0D9B2", "#818053", "#6B3848", "#8B3E50", "#D5BB6C", "#3F3A4B", "#474C66", "#A5806F"],
    "Levine2"     : ["#E3C1CB", "#AD5A6B", "#C993A2", "#365C83", "#384351", "#4D8F8B", "#CDD6AD"],
    "Liu"         : ["#9fd7bd", "#9b5c1c", "#97c124", "#3b5f13", "#ddb25d", "#5c4a32"],
    "Lupi"        : ["#61bea4", "#b6e7e0", "#aa3f5d", "#daa5ac", "#98a54f", "#2e92a2", "#ffb651", "#d85a44"],
    "Ohchi"       : ["#582851", "#40606d", "#69a257", "#e3d19c", "#c4024d"],
    "OKeeffe"     : ["#f3d567", "#ee9b43", "#e74b47", "#b80422", "#172767", "#19798b"],
    "Palermo"     : ["#1b80ad", "#ea5b57", "#9c5555", "#0c3c5f"],
    "Panton"      : ["#e84a00", "#bb1d2c", "#9b0c43", "#661f66", "#2c1f62", "#006289", "#004759"],
    "Picabia"     : ["#53362e", "#744940", "#9f7064", "#c99582", "#e6bcac", "#e2d8d6", "#a5a6ae","#858794", "#666879", "#515260", "#3d3d47"],
    "Picasso"     : ["#d5968c", "#c2676d", "#5c363a", "#995041", "#45939c", "#0f6a81"],
    "Rattner"     : ["#de8e69", "#f1be99", "#c1bd38", "#7a9132", "#4c849a", "#184363", "#5d5686", "#a39fc9"],
    "Sidhu"       : ["#af4646", "#762b35", "#005187", "#251c4a", "#78adb7", "#4c9a77", "#1b7975"],
    "Smith"       : ["#ef7923", "#75bca9", "#7b89bb", "#e9de97", "#2a2e38"],
    "ustwo"       : ["#d7433b", "#f06a63", "#ff8e5e", "#ffcc3d", "#95caa6", "#008d98"],
    "VanGogh"     : ["#c3a016", "#c3d878", "#58a787", "#8ebacd", "#246893", "#163274", "#0C1F4b"],
    "vonHeyl"     : ["#f96149", "#ffa479", "#e7d800", "#94aec2", "#0d0c0b"],
    "Warhol"      : ["#ff0066", "#328c97", "#d1aac2", "#a5506d", "#b3e0bf", "#2A9D3D", "#edf181", "#db7003", "#fba600", "#f8c1a6", "#A30000", "#ff3200", "#011a51", "#97d1d9", "#916c37"],
}

_sequential = {
    "Alkalay1",
    "Alkalay2",
    "Althoff",
    "Ernst",
    "Exter",
    "Flash",
}

_diverging = {
    "Avedon", 
    "Kippenberger",
    "Picabia"
}

_colorblind_friendly = {
    "Alkalay1",
    "Alkalay2",
    "Althoff",
    "Andri",
    "Connors",
    "Doughton",
    "Ernst",
    "Exter",
    "Flash",
    "Fritsch",
    "Kippenberger",
    "Koons",
    "Levine2",
    "Ohchi",
    "OKeeffe",
    "Palermo",
    "Picabia",
    "Picasso",
    "Rattner",
    "Sidhu",
    "Smith",
    "ustwo",
    "VanGogh",
    "vonHeyl"
}
