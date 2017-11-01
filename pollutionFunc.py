import classes
import initial
import numpy as np

def envirPoll(ambient_pollution, energy, pollution, absorbtionRate, dt):
	return ambient_pollution*energy*absorbtionRate*dt


