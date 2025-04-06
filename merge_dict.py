dict1={}
dict2={}
merge_dict={}
def input_data(dict_name):
    dictionary={}
    limit = int(input(f"enter the limit for data in {dict_name}:"))
    print(f"enter data to {dict_name} ")
    for x in range(limit):
        key = input("enter the key :")
        value = input("enter the value : ")
        dictionary[key]=value
    return  dictionary

def display(dict):
    for key,value in dict.items():
        print(f"{key}:{value}") 

dict1=input_data("dict1")
dict2=input_data("dict2")

merge_dict = {**dict1,**dict2}
print("first dictionary :")
display(dict1)
print("second dictionary :")
display(dict2)
print("merged dictionary :")
display(merge_dict)


        
    