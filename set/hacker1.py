n=int(input())
setA=set(map(int,input().split()))
m=int(input())
count=0
setB=set(map(int,input().split()))
for i in setA:
 if i in setB:
        count=count+1
if(count==len(setA)):
    print("True")
else:
    print("False")