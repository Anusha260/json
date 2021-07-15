import json

dic={}
file=open("Text.txt","r")
for line in file:
    key,value=line.strip().split(None,1)
    dic[key]=value.strip()
print(dic)
