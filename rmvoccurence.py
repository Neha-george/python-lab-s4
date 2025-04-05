list=[]
new_list=[]
limit =input("enter limit to the list:")
for x in range(0,limit+1):
    num = input("enter a number : ")
    list.append(num)
for num in list :
    if num not in new_list:
        new_list.append(num)
print("the original list is : ",list)
print("the new list is : ",new_list)