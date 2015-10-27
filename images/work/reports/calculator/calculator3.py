#This is a conversion calculator for Laser S/N : 400
#This calculator will tell you how many shots to get a desired overlap %

print("ROTARY SHOT-OVERLAP CALCULATOR")

shots = float(input("SHOTS FOR 360 DEGREES: "))
overlap = float(input("DESIRED OVERLAP %: "))

conversion = float(overlap) * float(.01)
conversion2 = float(conversion) * float(shots)
conversion3 = float(conversion2) + float(shots)

print (conversion3, "TOTAL SHOTS FOR", overlap, "%", "OVERLAP")

print ("Press Enter to Exit...")
input()

