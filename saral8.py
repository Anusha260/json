import json
a=["neelam","programer","24","24000"]
b=["komal","trainer","24","20000"]
c=["anu","HR","21","40000"]
d=["sindhu","manager","22","63000"]
e=["name","destination","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict={}
i=0
while i<len(a):

    dict1[e[i]]=a[i]
    dict2[e[i]]=b[i]
    dict3[e[i]]=c[i]
    dict4[e[i]]=d[i]
        
    dict["employe1"]=dict1
    dict["employe2"]=dict2
    dict["employe3"]=dict3
    dict["employe4"]=dict4
    i=i+1
print(dict)
# file=open("course.json","w")
# json.dump(dict,file,indent=4)




