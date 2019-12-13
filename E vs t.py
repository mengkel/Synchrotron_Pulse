#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:30:24 2019

@author: mengke
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
from IPython.display import HTML

beta = 0.8
omega = 1
q = 1.6*10**-19
c = 3*10**8
R=50

def update_points(num):
    point_ani.set_data(t[num], E[num])
    text_pt.set_position((t[num], E[num]))
    text_pt.set_text("t=%.1f, E=%.1e"%(t[num], E[num]))
    return point_ani,text_pt,

t = np.linspace(-np.pi, np.pi, 256)
E = -q*omega*beta*(beta-np.cos(t))/(1-beta*np.cos(t))**3/c/R
fig = plt.figure()

axes = fig.add_subplot(111) 

plt.plot(t,E)
point_ani, = plt.plot(t[0], E[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(1.2, 1.9, '', fontsize=10)

ani = animation.FuncAnimation(fig, update_points, np.arange(0, 1000), interval=20, blit=False)
plt.show()