limit = int (input("enter the limit of list : "))
k = int(input("enter the position by which we want to rotate :"))
list =[]
rotated_list =[]
for x in range(limit):
    num = int(input(f"enter element {x+1} :"))
    list.append(num)
k=k%limit
rotated_list =list[-k:]+list[:-k]
print(f"rotated list by {k} position is : {rotated_list}")
