lower_range = int(input("enter the lower range:"))
upper_range = int(input("enter the upper range:"))
evensum=oddsum=0
for x in range(lower_range,upper_range+1):
    if x%2==0:
        evensum+=x
    else:
        oddsum+=x
print("sum of even numbers in the given range is : ",evensum )
print("sum of odd numbers in the given range is : ",oddsum )