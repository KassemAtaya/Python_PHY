#Kassem ATAYA
#09/26/2022
#PHY 218
#CENGAGE QUESTIONS AND ANSWERS
#HOMEWORK_3_question9

##################################################################################### Sample question
import math
#variables
cu = -32 #uniformly distributed charge uC
cu = cu*(10**-6) # C
rR = 18 #spherecal volume radius
eq = 8.85*(10**-12)
k = 9*(10**9)
pi = math.pi


a = 9
b = 14
c = 34
########################################################
q = (cu*(a**3))/(rR**3)
r = a/100
eE = (q*k)/ r**2
print("(a) {}cm : answer : {}".format(a,eE))
q = (cu*(b**3))/(rR**3)
r = b/100
eE = (q*k)/ r**2
print("(b) {}cm : answer : {}".format(b,eE))


q = (cu*(c**3))/(rR**3)
r = c/100
eE = (cu*k)/ r**2
print("(c) {}cm : answer : {}".format(c,eE))
