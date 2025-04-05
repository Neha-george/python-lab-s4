num = int(input("enter the number for which multiplication table is to be found : "))
limit = int (input("enter the limit upto which table should be found : "))
for x in range(1,limit+1):
    print(num,"*",x ,"=",num*x)