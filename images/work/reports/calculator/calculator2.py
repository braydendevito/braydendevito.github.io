#This is a conversion calculator for Laser S/N : 400
#This calculator converts rotary speeds to linear speeds.

print("ROTARY-LINEAR CONVERSION")

dps = float(input("DEGREES PER SECOND: "))
diameter = float(input("DIAMETER OF PART: "))

circumference = float(diameter) * float(3.14159265359)


ips = float(circumference) * float(dps) / 360


print (ips,"INCHES/SEC")
print (float(ips) * float(60), "INCHES/MIN")

print ("Press Enter to Exit...")
input()
