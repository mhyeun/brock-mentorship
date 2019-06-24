#Appendix G: A planetary orbit code
#Brock Mentorship
#by Matthew Hyeun

#Version 2.4 (no steps printed out)



import math
import matplotlib.pyplot as plt



#Constants

G = 6.67 * 10**-11 #Gravitational constant
Msun = 1.99 * 10**30 #Mass of sun
AU = 1.496 * 10**11 #AU conversion to meters
spyr = 3.154 * 10**7 #Seconds per year


#User inputs

Mstrsun = float(input("Enter mass of the parent star, in solar masses: "))
print( )

aau = float(input("Enter semimajor axis of the orbit, in AU: "))
print()

e = float(input("Enter the eccentricity of the orbit: "))
print()


#Orbital period calcuation

Pyears = math.sqrt(aau ** 3 / Mstrsun)
Pyears = round(Pyears, 2)
print("The orbital period is", Pyears, "years.")
print( )


#User inputs for time steps and frequency of time steps

print("If too large of a time step is inputted, inaccurate results will be produced.")
print("If a high number of time steps is inputted, accurate results will be produced.")
print()

end = float(input("Enter the desired distance from the parent star for the calculation in AU: "))
print()

n = int(input("Enter the number of time steps for the calculation: "))
print()

kmax = 1


#Conversion to cgs units

period = Pyears * spyr
dt = period / (n - 1) #since first and last step is the same step
a = aau * AU
Mstar = Mstrsun * Msun


#State variables for loop

k = 0 #time step counter
theta = 0.00 #angle
time = 0.00 #self explanatory

#MAIN LOOP

data = []
data2 = []

for i in range(1, n):

    k = k + 1

    r = (a * (1 - e ** 2)) / (1 + e * math.cos(theta))

    if r >= (end * AU) or i == n:
        break

    #Calculate angluar momentum per unit mass L/m

    LoM = math.sqrt(G * Mstar * a * (1.00 - e ** 2))

    #Calculate next value of theta

    dtheta = LoM / r ** 2 * dt
    theta = theta + dtheta

    #Update elapsed time

    time = time + dt

    if k == kmax:
        k = 0

    x = r * math.cos(theta) / AU
    x = round(x, 2)


    y = r * math.sin(theta) / AU
    y = round(y, 2)

    data.append(x)
    data2.append(y)


#CONCLUSIONS

print("The calculation is complete.")
print()

x = r * math.cos(theta) / AU
x = round(x, 2)


y = r * math.sin(theta) / AU
y = round(y, 2)

        
print("x is equal to", x, "AU.")
print("y is equal to", y, "AU.")
print()

tyears = time/spyr
tyears = round(tyears, 2)
print(tyears, "years have elapsed to reach a distance of", end, "AU from the Sun.")


#GRAPH 
plt.xlabel('X-Value of Orbit (AU)')
plt.ylabel('Y-Value of Orbit (AU)')
plt.title('Orbit of Planet')


plt.plot(data, data2, "ro")
plt.show()
