tup1 = map(int,(input("enter the elements of tuple1 separated by space : ").split()))
tup2 = map(int,(input("enter the elements of tuple2 separated by space : ").split()))
is_subset = True
for element in tup2:
    if element not in tup1:
        is_subset =False
        break
if is_subset:
    print("tuple2 is a subset of tuple1")
else:
    print("tuple2 is not a subset of tuple1")
