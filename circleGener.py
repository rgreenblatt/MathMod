#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import argparse
from typing import List, Tuple
from math import sqrt


def collect(x: int, y: int, sigma: float =3.0) -> List[Tuple[int, int]]:
    """ create a small collection of points in a neighborhood of some point 
    """
    neighborhood = []

    X = int(sigma)
    for i in range(-X, X + 1):
        Y = int(pow(sigma * sigma - i * i, 1/2))
        for j in range(-Y, Y + 1):
            neighborhood.append((x + i, y + j))

    return neighborhood


def gener(radius):
	#returns convolutional kernal for a circle
	x = np.linspace(-radius, 1, radius)
	y = np.linspace(-radius, 1, radius)
	xv, yv = np.meshgrid(x, y)
	val = xv*xv+yv*yv
	weight = 1-np.sqrt(val)/radius
	convolve = np.where(weight>0,weight,0)
	return convolve

