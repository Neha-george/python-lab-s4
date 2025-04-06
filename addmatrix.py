r1 = int(input("enter the row number for 1 st matrix:"))
c1 = int(input("enter the column number for 1 st matrix:"))
r2 = int(input("enter the row number for 2nd matrix:"))
c2 = int(input("enter the column number for 2nd matrix:"))
matrix1=[]
matrix2=[]
result=[]
if r1!=r2 and c1!=c2:
    print("addition is not possible")
else:
    print("enter the elements for first matrix ")
    for i in range (r1):
        row1=[]
        for j in range (c1):
             num = int(input(f"enter the element({i+1},{j+1}) : "))
             row1.append(num)
        matrix1.append(row1)
    print("enter the elements for second matrix ")
    for i in range (r2):
        row2=[]
        for j in range (c2):
             num = int(input(f"enter the element({i+1},{j+1}) : "))
             row2.append(num)
        matrix2.append(row2)
    for i in range (r1):
        row_sum=[]
        for j in range (c1):
            row_sum.append(matrix1[i][j]+matrix2[i][j])
        result.append(row_sum)

print("first matrix")
for row in matrix1:
    print(row)
print("second matrix")
for row in matrix2:
    print(row)
            
print("\nResultant Matrix:")
for row in result:
        print(row)