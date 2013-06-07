from particle import *

def printPos(arr):
    for a in arr:
        print(str(a.pos))
        
def initialize(n, numParticles, temp):
    parts = []
    for i in range(0, numParticles):
        p = Particle()
        
        p.mass = 1
        p.pos = [0] * n
        p.vel = [0] * n
        for j in range(0, n):
            p.pos[j] = 1    #random linear
            vDist = getBoltzmannsDistArray(p.mass, tmep, n)
            p.vel[j] = vDist[random.randint(0, len(vDist))]
#            p.vel[j] = tempToVelocity(temp, mass)    #maxwell boltzmann dist for init temp
        parts.append(p)
    return parts



particles = initialize(2, 10, 293)
t = 1
t2 = t ** 2
 
printPos(particles)   
    
print("apply force")

for part in particles:
    part.update(t, t2, [1,1,1])
    
printPos(particles)

