#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:54:32 2019

@author: mengke
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r=2.0
a,b = (0., 0.)
t = np.arange(0.5*np.pi, 2.5*np.pi, 0.01)

def update_points(num):
    point_ani.set_data(x[num], y[num])
    text_pt.set_position((x[num], y[num]))
    text_pt.set_text("x=%.1f, y=%.1f"%(x[num], y[num]))
    return point_ani,text_pt,

x = a + r*np.cos(t)
y = b + r*np.sin(t)
fig = plt.figure()

axes = fig.add_subplot(111) 
axes.axis('equal')
plt.plot(x,y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(0.5, 0.5, '', fontsize=10)

ani = animation.FuncAnimation(fig, update_points, np.arange(0, 1000), interval=20, blit=False)
plt.show()