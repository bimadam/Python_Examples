#Created by Adam Bím
#11/2021

import math
import time

welcomemessage = ("""
Skript pro výpočet kvadratické rovnice
""")
print (welcomemessage)
print (" ")

time.sleep (2)

a = int(input("Zadej hodnotu a: "))
b = int(input("Zadej hodnotu b: "))
c = int(input("Zadej hodnotu c: "))

time.sleep (2)
print (" ")

# výpočet diskriminantu
d = pow(b, 2) - 4 * a * c

# pokud diskriminant = 0
if d == 0:
    x0 = -b / (2 * a) if a != 0 else 0
    print("Rovnice má jedno řešení x1 =", x0)

# pokud diskriminant > 0
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a) if a != 0 else 0
    x2 = (-b - math.sqrt(d)) / (2 * a) if a != 0 else 0
    print("Rovnice má dvě řešení x1 =", x1, "a x2 =", x2)

# pokud diskriminant < 0
elif d < 0:
    print("Rovnice nemá řešení v oboru reálných čísel!")

print (" ")
endmessage = ("""
Díky za použití kalkulačky!
""")
print (endmessage)