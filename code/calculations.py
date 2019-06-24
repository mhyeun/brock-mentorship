#Brock Mentorship Project
#Celestial Mechanics Question 2.11
#Halley's Comet
#by Matthew Hyeun

import math

    
Period = 0
Eccentricity = 0
Semimajoraxis = 0

a = 0 #semimajor axis in AU
ameters = 0 #semimajor axis in m
mSun = 0 #mass of sun

rp = 0 #perihelion
ra = 0 #aphelion
rpmeters = 0 #perihelion in meters

vp = 0 #velocity at perihelion
va = 0 #velocity at aphelion
b = 0 #seminimor axis
vb = 0 #velocity at semiminor axis
c = 0 #distance from semiminor axis to focus

deltaV = 0 #difference of velocities

G = 6.67 * 10**-11 #gravitational constant




Period = float(input("What is the orbital period of your mass, in years? ")) #Orbital Period, in years
print("The orbital period of your mass has been inputted as", Period, "years. \n")

Eccentricity = float(input("What is the orbital eccentricity of your orbit? ")) #Eccentricity
print("The orbital eccentricty of your orbit has been inputted as " + str(Eccentricity) + ".\n")




#Question (a) - What is the semimajor axis of the orbit?

print("Question A:")
print("What is the semimajor axis of the orbit of your mass?\n")

print("Kepler's Third Law states that: p**2 = a**3;")
print("where p is equal to the orbital period in years, and a is the semimajor axis in AU.")
print("You have inputted that your orbital period is", Period, "years.")
print("Using this, we can find that: \n")

a = (Period ** 2) ** (1 / 3)
a = round(a, 4)

print("The semimajor axis of your orbit is", a, "AU (Astronimical Unit).\n")




#Question (b) - Use your mass to estimate the mass of the sun.

print("Question B:")
print("Use your mass to estimate the mass of the sun. \n")


    #Kepler's Third Law also states that: P**2 = ( 4 * π**2 * a**3 ) / ( G (m1 + m2) )
    #m2 in this case is negligable, because m1 + m2 is nearly equal to m1.
    #G is the gravitational constant; 6.67 * 10**-11.

print("The semimajor axis must be converted into metres.")
ameters = a * 149597870700 #conversion factor for AU to m
print("Your semimajor axis is", "%.3e" % ameters, "meters. \n")


print("The period must be converted into seconds.")
periodseconds = Period * 31556926 #conversion factor from yrs to s
print("Your period is", "%.3e" % periodseconds, "seconds. \n")

print("The program will now estimate the mass of the sun, assuming that m2 is negligable. \n")

mSun = ( 4 * math.pi**2 * ameters**3 ) / ( G * periodseconds**2)

print("The estimated mass of the sun is", "%.3e" % mSun, "kilograms. \n")




#Question (c) - Calculate the distance from the Sun at perihelion and aphelion.

print("Question C: ")
print("Calculate the distance from the Sun at perihelion and aplhelion. \n")

a = float(a)
Eccentricity = float(Eccentricity)

rp = a * ( 1 - Eccentricity ) #formula for perihelion
rp = round(rp, 4)

print("The distance from the Sun at perihelion is", rp, "AU. \n")


ra = a * ( 1 + Eccentricity ) #formula for aphelion
ra = round(ra, 4)

print("The distance from the Sun at aphelion is", ra, "AU. \n")




#Question (d) - Calculate the orbital speed at perihelion, aphelion, and at semiminor axis.

print("Question D: ")
print("Calculate the orbital speed at perihelion, aphelion, and at semiminor axis. \n")

vp = math.sqrt(((G * mSun) / ameters ) * ((1 + Eccentricity) / (1 - Eccentricity))) #velocity at perihelion
print("The orbital speed at perihelion is", "%.4e" % vp, "meters per second. \n")

va = math.sqrt(((G * mSun) / ameters ) * ((1 - Eccentricity) / (1 + Eccentricity))) #velocity at aphelion
print("The orbital speed at aphelion is", "%.4e" % va, "meters per second. \n")

  #semiminor axis

b = math.sqrt(( ameters ** 2) * ( 1 - (Eccentricity ** 2)))
print("The semiminor axis of the orbit is", "%.4e" % b, "meters.")

c =  math.sqrt(( b ** 2 ) + (( ameters - rp ) ** 2 ))
print("The distance from the semiminor axis to the sun is", "%.4e" % c, "meters.")

rpmeters = rp * 149597870700 #conversion factor from AU to m

vb = math.sqrt( 2 * ((( 1 / 2 ) * ( vp ** 2 )) - ( G * ( mSun / rpmeters )) + (G * ( mSun / c ))))

print("The orbital velocity at semiminor axis is", "%.4e" % vb, "meters per second. \n")



#Question (e) - Compare the kinetic energy of the comet at perihelion and aphelion.

print("Question E: ")
print("Compare the kinetic energy at perihelion and aphelion. \n")

      #K = (1/2) mu v^2 ; we can cancel out (1/2), and mu.

deltaV = ( vp / va ) ** 2

print("The difference of kinetic energy at perihelion and aphelion is equal to " + "%.4e" % deltaV + ".")
