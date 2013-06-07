from math import *
import random

def gaussienDist():
   return 0 

def boltzmannsDist(v, mass, temp, n):
    #implement integral
    return (mass/(2.0*pi*k*temp))**(n/2.0)*exp(-mass*v)

def getBoltzmannsDistArray(mass, temp, n):
    k = 1.3806e-23
    v = []
    dv = 0.1
    i = 1
    maxV = 100
    pastLowerTail = 0
    prob = boltzmannsDist(dv)
    while prob > 0.01 and pastLowerTail > 0:
        prob = boltzmannsDist(dv*i, dv, n)
        for j in range(0, floor(prob*100)):
            v.append(dv*i)
        i = i + 1
        if pastLowerTail < 1 and prob > 0.01:
            pastLowerTail = 1
    return v

def tempToVelocity(vDist):
    #maxwell dist
    return 0