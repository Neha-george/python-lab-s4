radius = float(input ("enter the radius of cylinder :"))
height = float(input("enter the height of cylinder : "))
def vol(radius,height):
    return 3.14*radius**2*height
def sa(radius,height):
    return 3.14*radius**2*(height+radius)
print("surface area of cylinder is : ",sa(radius,height))
print("volume of cylinder is : ",vol(radius,height))