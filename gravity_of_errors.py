#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A Study of the Utmost Gravity

A set of functions to calculate the effects of gravity.

Created on Mon Jun 17 18:28:40 2019

@author: aanderson
"""

def drag(A, v):
    """Air drag on object
        A = cross-sectional area
        v = velocity as tuple (vx,vy)"""
        dv = -A * v

def xy(t, xy0, v0):
    """This function calculates the trajectory of an object
    under the influence of Earth's gravity near its surface:

        xy(t, (x0,y0), (vx0,vy0))

    where xy, x0, and y0 are in meters and vx0 and vy0 are in meters/second."""
    g = 9.81
    # split tuples into components for vector addition and scalar multiplication
    (x0,y0) = xy0
    (vx0,vy0)= v0
    return x0 + vx0 * t, y0 + vy0 * t + 1./2 * g * t**2

try:
    xy0 += (0,0)
except (NameError, TypeError):
    x0 = float(input("Initial position x0 = "))
    y0 = float(input("Initial position y0 = "))
    xy0 = (x0, y0)

try:
    v0
except (NameError, TypeError):
    vx0 = float(input("Initial speed vx0 = "))
    vy0 = float(input("Initial speed vy0 = "))
    v0 = (vx0, vy0)
finally:
    try:
        trajectory = [(t/2.,) + xy(t/2., xy0, v0) for t in range(8)]
    except:
        print("data has problems: " + str(xy0))


print(trajectory)

