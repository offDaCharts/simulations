from particle import *

def printPos(arr):
    for a in arr:
        print(str(a.pos))
        
def initialize(n, numParticles):
    parts = []
    for i in range(0, numParticles):
        p = Particle()
        
        p.pos = [0] * n
        p.vel = [0] * n
        for j in range(0, n):
            p.pos[j] = 1    #random linear
            p.vel[j] = 1    #maxwell boltzmann dist for init temp
        parts.append(p)
    return parts



particles = initialize(2, 10)
t = 1
t2 = t ** 2
 
printPos(particles)   
    
print("apply force")

for part in particles:
    part.update(t, t2, [1,1,1])
    
printPos(particles)

