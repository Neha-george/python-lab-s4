limit = int(input("enter limit of tuple :"))
tup=()
eventup=()
oddtup=()
print("enter elements to the tuple")
for x in range(limit):
    num = int(input(f"enter element{x+1} :"))
    tup=tup+(num,)
for element in tup:
    if element%2==0:
        eventup=eventup+(element,)
    else:
        oddtup=oddtup+(element,)
print("the given tuple :",tup)
print("even elements in the given tuple are :",eventup)
print("odd elements in the given tuple are :",oddtup)