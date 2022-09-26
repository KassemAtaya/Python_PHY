#Kassem ATAYA
#09/26/2022
#PHY 218
#CENGAGE QUESTIONS AND ANSWERS
#HOMEWORK_3_question3

##################################################################################### Sample question

# The diagram shows a closed triangular prism situated in a region of uniform electric field 
# E = (6.84 ✕ 10^44 ĵ) N/C.


#The dimensions of the triangular prism are a = 17.4 cm,b = 10.0 cm,d = 29.8 cm.Note that the diagram is not to scale.
e = 6.84*(10**4) #N/C
a = 17.2 #cm
b = 10.0 #cm
d = 34.2 #cm

import math
a = a/100 #m
b = b/100 #m
d = d/100 #m
 

print("(a) What is the flux through the bottom face of the triangular prism?\n")
p = math.cos(math.radians(180))
answer1 = e*a*d*p

print("answer1 :  {} N . m^2/C\n".format(answer1))

#########################################################
print("(b) The slanted rectangular surface\n")
c = math.sqrt(a**2 + b**2)
p = math.cos(math.radians(29.9))
answer2 = e*c*d*p

print("answer2 :  {} N . m^2/C\n".format(answer2))

#########################################################
print("(c) The front triangular surface: The normal to this surface is out of the page.\n")
answer3 = 0 
print("answer3 :  {} N . m^2/C\n".format(answer3))

#########################################################
print("(d) The back triangular surface:.\n")
answer4 = 0 
print("answer4 :  {} N . m^2/C\n".format(answer4))
#########################################################
print("(e) The vertical rectangular surface\n")
answer5 = 0 
print("answer5 :  {} N . m^2/C\n".format(answer5))

########################################################
print("(f) total flux\n")
answer6 = answer1+answer2+answer3+answer4+answer5
print("answer6 :  {} N . m^2/C\n".format(answer6))

