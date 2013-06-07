from globals import *

class Particle:
    def __init__(self, species, n):
        self.dimensions = n
        self.pos = [0] * n
        self.vel = [0] * n
        self.species = species
        self.mass = massDict[species]
        self.charge = 0
        
        if (speed**2.0 * self.mass)/2.0 > deutIonEnergy:
            self.charge = 1
        else:
            self.charge = 0
    
    def update(self, dt, dt2, force):
        for i in range(0, len(self.pos)):
            self.pos[i] = self.pos[i] + self.vel[i] * dt + 1/2 * force[i] * self.mass * dt2

        for i in range(0, len(self.vel)):
            self.vel[i] = self.vel[i] + force[i] * self.mass * dt
        
        speed = numpy.linalg.norm(self.vel)
        if (speed**2.0 * self.mass)/2.0 > deutIonEnergy:
            self.charge = 1
        else:
            self.charge = 0

