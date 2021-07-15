import json

user=int(input("enter the user"))

dict1={}
dict2={}
i=0
while i<user:
    user1=input("enter the input:")
    num=int(input("enter the num"))
    dict2[user1]=num
    i+=1
dict1["shopping_list"]=dict2
print(dict1)
with open("shopping_list","w") as f:
    json.dump(dict1,f,indent=4)

