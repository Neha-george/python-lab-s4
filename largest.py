a,b,c =map(int,(input("Enter 3 numbers separated by space: ").split()))
if a>b:
    if a>c:
        print(a , "is the largest")
    else:
        print(c , "is the largest")
else:
    if b>c:
        print(b , "is the largest")
    else :
        print(c, "is the largest")