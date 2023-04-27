# dict always contains key value pairs and from python version 3.7 dictonaries are ordered in python version 3.6 
# and earlier it is unordered

#DEFINE EMPTY DICT
info={}

#ASIGNMEN TO DICT
info={1:'muskan',2:'someone',3:'otherone',4:'noone'}

#GET VALUES BY KEY
#1...
print(info[2])
# print(info[5]) #it will return a key error because 5 key is not present in dict

#2...
print(info.get(2))
print(info.get(5)) #it returns none when key is not present in dict

#3...for complete dict with key value pair
print(info)

# DICT IS CHANGEABLE
info[3]='pandey'
print(info,"change")

#DUPLICATES NOT ALLOWED
info[5]='pandey' #value is same here but keys are different so its not duplicate
print(info,"dupli") 

#HOW TO GET ALL KEYS OF DICT
print(info.keys())

# it gives all the value to the corresponding keys
for i in info.keys():
    print(info[i]) 
#using formt string
    print(f"The value of {i} is {info[i]}")

#HOW TO GET ONLY VALUES WITHOUT ANY KEY
print(info.values())

#HOW TO GET BOTH KEYS AND VALUES 
for key,value in info.items():
    print(f"the value of {key} is {value}")
