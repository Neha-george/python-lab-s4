dict ={}
def display_dict():
    for bname,bstock in dict:
        print(f"{bname}:{bstock}")

while True:
    print("MENU")
    print("1.add stock")
    print("2.update stock")
    print("3.delete stock")
    print("4.exit")
    ch = int(input("enter yur choice : "))
    if ch==1:
        while True:
            bname = input("enter the book name : ")
            bstock = int(input("enter the corresponding stock : "))
            dict[bname]=bstock
            display_dict()
            ch1=input("do you want to add more books?(y/n): ")
            if ch1=="n":
                break
    elif ch==2:
        bname = input ("enter the book name : ")
        if bname in dict :
            x=dict[bname]
            new_stock = int(input("enter the new stock: "))
            dict[bname]=x+new_stock
            display_dict()
    elif ch==3:
        bname =input("enter the book name :")
        if bname in dict:
            del dict[bname]
            print(f"{dict[bname]} deleted from dictionary")
            display_dict()
    elif ch==4:
        break
    else:
        print("enter a valid choice !!")
