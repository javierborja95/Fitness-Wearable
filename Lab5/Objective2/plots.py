# Imports
import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(211)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
y1 = np.cos(X)
y2 = np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, y1, color="blue", linewidth=1.0, linestyle="-")

# Set y ticks
plt.yticks(np.linspace(-1,1,3,endpoint=True))

#Set x axis
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])

plt.subplot(212)

# Plot sine using red color with a continuous line of width 1 (pixels)
plt.plot(X, y2, color="red", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-np.pi,np.pi)

# Set x ticks
plt.xticks(np.linspace(-np.pi,np.pi,5,endpoint=True))

# Set y limits
plt.ylim(-1.0,1.0)

# Set y ticks
plt.yticks(np.linspace(-1,1,3,endpoint=True))

#Set x axis
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])

# Show result on screen
plt.show()

''' a(sinx) and a(cosx) together '''