import globals
from globals import *
from distributions import *
from particle import *

def printPos(arr):
    for a in arr:
        print(str(a.pos))

def printVel(arr):
    for a in arr:
        print(str(a.vel))
        
def printCharge(arr):
    for a in arr:
        print(str(a.charge))
        
def initialize(n, numParticles, temp):
    parts = []
    max = [1000] * n
    
    for i in range(0, numParticles):
        p = Particle("dueterium", n)
        for j in range(0, n):
            p.pos[j] = random.random() * max[j]
            p.vel[j] = tempGaussienDist(temp, p.mass)


#            vDist = getBoltzmannsDistArray(p.mass, temp, n)
#            p.vel[j] = vDist[random.randint(0, len(vDist))]
#            p.vel[j] = tempToVelocity(temp, mass)    #maxwell boltzmann dist for init temp
        parts.append(p)
    return parts

def createMatrices(n):
    #D = numpy.diagflat([-1]*(n-1),1) + numpy.diagflat([4]*n,0) + numpy.diagflat([-1]*(n-1),-1)
    #negI = numpy.diagflat([-1]*(n),0)
    diag = [-1]*(n**2-1)
    for i in range(1,n):
        diag[i*n-1] = 0
    A = numpy.diagflat(diag,1) + numpy.diagflat([4]*n**2,0) + numpy.diagflat(diag,-1)
    B = numpy.diagflat([-1]*(n**2-n),n) + numpy.diagflat([-1]*(n**2-n),-n)
    A = A + B
    return A
        
    
def calculateForce(p):
    

    
    return 0



particles = initialize(2, 10, 293)
t = 1
t2 = t ** 2

print "position"  
printPos(particles)  
print "velocity" 
printVel(particles)   
print "charge" 
printCharge(particles)   
    
print("apply force")

for part in particles:
    part.update(t, t2, [1,1])
    
print "position"  
printPos(particles)
print "velocity"
printVel(particles)
print "charge" 
printCharge(particles)   

