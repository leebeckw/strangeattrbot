import random
from math import log2, sqrt

# lots of this very beautiful & clean code is adapted from this repository:
# https://github.com/icecolbeveridge/strangeAttractors
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXY"

generateAttrString = lambda n: "".join( [random.choice(LETTERS) for i in range(n)])

letterToNumber = lambda x: 0.1*(LETTERS.index(x) - 12)

# get the next value in the series
def nextVal( x, y, params ):
    a,b,c,d,e,f = params
    return a + b*x + c*x*x + d*x*y + e*y + f*y*y

# generate a chaotic set of coefficients
def generateAttractor(init = (0.05,0.05) ):
    attrString = generateAttrString(12)
    
    print(attrString)
    xparams = list(map(letterToNumber, attrString[:6]))
    yparams = list(map(letterToNumber, attrString[6:]))

    x,y = init

    # initial iteration to check for divergence to infinity
    for i in range(100):
        x,y = nextVal(x,y,xparams), nextVal(x,y,yparams)
        
        # check for divergence to infinity
        if abs(x) > 1.e5:
            return None

    lyapunov = 0
    
    x1 = x
    y1 = y
    x2 = x + 10e-6
    y2 = y

    # calculate lyapunov exponent after 11000 iterations
    for j in range(1,11000):
        results = calculateLyapunov(x1, y1, x2, y2, xparams, yparams)
        to_add = results[0]
        x1 = results[1]
        y1 = results[2]
        x2 = results[3]
        y2 = results[4]
        lyapunov = (lyapunov + to_add)
    
    lyapunov = 1/j * lyapunov
    
    # check for chaotic behavior
    if lyapunov > 0.001:
        print(lyapunov)
        return attrString
    else:
        return None
        
# helper fn to calculate euclidian distance
def calculateDistance(x1, y1, x2, y2):
    xdist_n = abs(x2 - x1)
    ydist_n = abs(y2 - y1)
    return sqrt(xdist_n**2 + ydist_n**2)

# calculate a term of the sum for the lyapunov exponent
def calculateLyapunov(x1, y1, x2, y2, xparams, yparams):
    dn = calculateDistance(x1, y1, x2, y2)
    x1new = nextVal(x1, y1, xparams)
    y1new = nextVal(x1, y1, yparams)
    x2new = nextVal(x2, y2, xparams)
    y2new = nextVal(x2, y2, yparams)
    dn1 = calculateDistance(x1new, y1new, x2new, y2new)
    if dn == 0 or dn1/dn == 0:
        log_to_add = 0
    else:
        log_to_add = log2(dn1/dn)
    return [log_to_add, x1new, y1new, x2new, y2new]

# given a string of coefficients, generate a certain number
# of points in the series to eventually graph
def generatePoints(s, num_iter=100000, init=(0.05, 0.05)):
    xparams = list(map(letterToNumber, s[:6]))
    yparams = list(map(letterToNumber, s[6:]))
    
    out = [init]
    x,y = init
    
    for k in range(num_iter):
        x,y = nextVal(x,y,xparams), nextVal(x,y,yparams)
        out.append((x,y))
    
    return out

def return_valid_coefficients(s=None):
    while s == None:
        s = generateAttractor()
    
    return s