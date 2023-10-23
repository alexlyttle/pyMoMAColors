import os
import numpy as np
import momacolors as moma
import matplotlib.pyplot as plt

imgdir = "images"
if not os.path.isdir(imgdir):
    os.makedirs(imgdir)

fig, axes = moma.show_all()
fig.savefig(os.path.join(imgdir, "colormaps.png"))

fig, axes = moma.show_all(sequential=True)
fig.savefig(os.path.join(imgdir, "sequential.png"))

fig, axes = moma.show_all(256, sequential=True)
fig.savefig(os.path.join(imgdir, "sequential_256.png"))

fig, axes = moma.show_all(256, diverging=True)
fig.savefig(os.path.join(imgdir, "diverging_256.png"))

fig, axes = moma.show_all(6, brew_type="continuous", colorblind_friendly=True)
fig.savefig(os.path.join(imgdir, "colorblind_6.png"))

fig, axes = moma.show_all(6, brew_type="discrete", colorblind_friendly=True)
fig.savefig(os.path.join(imgdir, "colorblind_6_discrete.png"))

fig, axes = moma.show_all(6, brew_type="continuous", colorblind_friendly=True)
fig.savefig(os.path.join(imgdir, "colorblind_6_continuous.png"))

cmap = moma.get_colormap("Abbott")
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott.png"))

cmap = moma.get_colormap("Abbott", n=20)
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott_20.png"))

cmap = moma.get_colormap("Abbott", n=20, brew_type="discrete")
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott_20_discrete.png"))

cmap = moma.get_colormap("Abbott", direction=-1)
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott_reversed.png"))

cmap = moma.get_colormap("Abbott", 4)
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott_4.png"))

cmap = moma.get_colormap("Abbott", 4, override_order=True)
ax = moma.plotting.plot_cmap(cmap)
plt.savefig(os.path.join(imgdir, "abbott_4_override.png"))

x = np.linspace(0, 2*np.pi, 101)
y = np.sin(x)
c = np.sin(x)**2

# Choose appropriate colormap
cmap = moma.get_colormap("Ernst", n=256)

fig, ax = plt.subplots()
s = ax.scatter(x, y, c=c, cmap=cmap)
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(s, label=r"$\sin^2(x)$")
