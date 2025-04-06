list=[]
limit = int(input("enter the limit to list : "))
for x in range(limit):
    print(f"for tuple {x+1} ")
    tup =()
    first=input(f"enter the first element  : ")
    tup+=(first,)
    second=input(f"enter the second element  : ")
    tup+=(second,)
    list.append(tup)

sorted_list =sorted(list,key=lambda x :x[1])
print("original list :",list)
print("sorted list :",sorted_list)

