#Kassem ATAYA
#09/26/2022
#PHY 218
#CENGAGE QUESTIONS AND ANSWERS
#HOMEWORK_3_question1

##################################################################################### Sample question 
# Consider the uniform electric field E = (7.0j + 9.0k)*10^3 N/C.
# What is its electric flux (in N.m^2/C) through a circular area of radius 3.0 m
# that lies in the xy-plane?(Enter the magnitude.)

#################################################################################### Variable implementation
#Enter your variables for j k and radius

j = 8
k = 7

r = 8 #radius

################################################################################ #Formulas used to solve question 
# The electric flux through a circular area formula is:
# ΦE = E*A
# Area of a circle formula is
# Area = π * r^2
################################################################################ #Inserting formula
import math

pi = math.pi


magnitude = (k*(10**3))* pi*(r**2)



print("{:.2f} N.m^2/C".format(magnitude))
