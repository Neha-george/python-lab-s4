string=input("enter the string to be reversed: ")
rev=""
for x in range(0,len(string)+1):
    rev=string[x]+rev
print("original word is :",string)
print("reversed word is :",rev)
