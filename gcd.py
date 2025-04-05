num1,num2 = map(int,(input("enter 2 numbers whose gcd is to be found separated by space :").split()))
small = min(num1,num2)
for x in range(1,small+1):
    if num1%x==0 and num2%x==0:
        gcd = x
print( "gcd of ",num1 ,",",num2, "is :",gcd )