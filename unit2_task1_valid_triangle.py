#triangle is valid given its three angles
print("Enter the three angles of the triangle:")
angle1 = float(input("Angle 1: "))
angle2 = float(input("Angle 2: "))
angle3 = float(input("Angle 3: "))
print("The sum of the angles is: ", angle1 + angle2 + angle3)
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")