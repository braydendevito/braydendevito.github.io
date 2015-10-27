#This is a conversion calculator for Laser S/N : 400
#Linear travel bead on plate feed rates are converted to rotary speed feed rates.
#The linear speed value is the feedrate G code called in the program marked by "Fx"

print("LINEAR-ROTARY CONVERSION CALCULATOR")
print ("ENTER THE LINEAR SPEED VALUE")
ips = float(input("INCHES PER SECOND: "))
circumference = float(input("DIAMETER OF PART: "))
diameter = float(circumference) * float(3.14159265359)
div1 = float(ips) / float(diameter)
dps = float(div1) * float(360)

print (dps, "DEGREES/SEC") #degrees per second
print (float(dps) * float(60), "DEGREES/MIN") #degrees per minute
print ("Press Enter to Exit...")
input()
