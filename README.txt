hi!

matlab to numpy:
http://mathesaurus.sourceforge.net/matlab-numpy.html

Solving Poisson (from http://en.wikipedia.org/wiki/Thomas_algorithm):

# note: function also modifies b[] and d[] params while solving
def TDMASolve(a, b, c, d):
    n = len(d) # n is the numbers of rows, a and c has length n-1
    for i in xrange(n-1):
        d[i+1] -= d[i] * a[i] / b[i]
        b[i+1] -= c[i] * a[i] / b[i]
    for i in reversed(xrange(n-1)):
        d[i] -= d[i+1] * c[i] / b[i+1]
    return [d[i] / b[i] for i in xrange(n)] # return the solutio