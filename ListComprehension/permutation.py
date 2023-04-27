
# A Python program to print all
# permutations using library function
list=[]
for i in range(3):
    value=int(input())
    list.append(value)
n=int(input())
def listMake(a):
    li=[]
    for s in range(a+1):
       li.append(s)
    return li
finalList=[listMake(a) for a in list] 
per=[[m,p,S] for m in finalList[0] for p in finalList[1] for S in finalList[2] if((m+p+S))!=n]
print(per)
 
 
 
 
 
 
 
 
 
 
 
 
# Get all permutations of [1, 2, 3]
# perm = permutations([1, 2, 3])
 
#  Print the obtained permutations
# for i in list(perm):
#     print (i)