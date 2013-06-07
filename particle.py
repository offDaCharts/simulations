class Particle:
    dimensions = 3
    pos = []
    vel = []
    mass = 2
    def update(self, dt, dt2, force):
        for i in range(0, len(self.pos)):
            self.pos[i] = self.pos[i] + self.vel[i] * dt + 1/2 * force[i] * self.mass * dt2

        for i in range(0, len(self.vel)):
            self.vel[i] = self.vel[i] + force[i] * self.mass * dt

