import math
pi = math.pi

ee = -9*(10**-6) #charge

r = 0.09 #radius
ep = 8.85*(10**-12)
w = 0.17 #point


o = ((ee/0.01)/(2*pi*r))
print(o)
e = (r*o)/(ep*w)
print(e)
