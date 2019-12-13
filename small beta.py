#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:17:41 2019

@author: mengke
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ((ax11, ax12)) = plt.subplots(1,2,
                                 sharex=False,
                                 sharey=False,
                                  tight_layout=False)
fig.subplots_adjust(wspace=0.3)

ax11.axis('equal')
ax11.set_xlabel('x')
ax11.set_ylabel('y',rotation=0)
ax11.set_title('electron motion')
ax12.set_xlabel('t')
ax12.set_ylabel('E(t)',rotation=0)

r=1
a,b = (0., 0.)
beta = 0.8
omega = 1
q = 1.6*10**-19
c = 3*10**8
R=50
ax12.set_title(r'$\beta$='+str(beta))
t = np.arange(-np.pi, np.pi, 0.05)
x = a + r*np.sin(t)
y = b - r*np.cos(t)
line11, = ax11.plot(x,y,lw=2)

E = -q*omega*beta*(beta-np.cos(t))/(1-beta*np.cos(t))**3/c/R
line12, = ax12.plot(t,E,lw=2)


def update_points(num):
    point_ani1.set_data(x[num], y[num])
    point_ani2.set_data(t[num], E[num])
    
    text_pt1.set_position((x[num], y[num]))
    text_pt2.set_position((t[num], E[num]))
    
    text_pt1.set_text("x=%.1f, y=%.1f"%(x[num], y[num]))
    text_pt2.set_text("t=%.1f, E=%.1e"%(t[num], E[num]))
    return point_ani1,point_ani2,text_pt1,text_pt2,


point_ani1, = ax11.plot(x[0], y[0], "ro")  
point_ani2, = ax12.plot(t[0], E[0], "ro")
ax11.grid(ls="--")
ax12.grid(ls="--")
text_pt1= plt.text(0.5, 0.5, '', fontsize=10)
text_pt2= plt.text(1.2, 1.9, '', fontsize=10)
 
ani = animation.FuncAnimation(fig, update_points, frames=500, interval=20, blit=False)
plt.show()