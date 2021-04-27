from numpy import linspace
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
  
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
  
t = np.linspace(0, 1, 1000, endpoint=True)
ax.plot3D(t, signal.square(2 * np.pi * 5 * t))
  
for angle in range(0, 360):
   ax.view_init(angle,30)
   plt.draw()
   plt.pause(.001)