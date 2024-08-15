import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

# Create the three stripes of the flag
a = patch.Rectangle((0, 1), width=9, height=2, facecolor='#FF9933', edgecolor='grey')
b = patch.Rectangle((0, 3), width=9, height=2, facecolor='#ffffff', edgecolor='grey')
c = patch.Rectangle((0, 5), width=9, height=2, facecolor='#138808', edgecolor='grey')

# Set up the figure and add the stripes
m, n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

# Create the Ashoka Chakra
radius = 0.8
py.plot(4.5, 4, marker='o', markerfacecolor='#000080', markersize=9.5)
chakra = py.Circle((4.5, 4), radius, color='#000080', fill=False, linewidth=7)
n.add_artist(chakra)

# Create the 24 spokes of the Ashoka Chakra
for i in range(0, 24):
    p = 4.5 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
    q = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
    r = 4.5 + radius * np.cos(np.pi*i/12)
    s = 4 + radius * np.sin(np.pi*i/12)
    t = 4.5 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
    u = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
    n.add_patch(patch.Polygon([[4.5, 4], [p, q], [r, s], [t, u]], fill=True, closed=True, color='#000080'))

# Remove the axis labels and ticks
n.set_xticks([])
n.set_yticks([])
n.axis('off')  # Hides the axis

# Set equal aspect ratio
py.axis('equal')

# Display the flag
py.show()
