n = int(input())
list = list(map(int, input().split()))
list.sort()
Listmax=max(list)
print(Listmax)
i=2
print(list[len(list)-2])
print(len(list))
print(len(list)-2)
while(n>i):
 if(list[len(list)-i]!=Listmax):
        secondMax=list[len(list)-i]
    i=i+1
print(secondMax)
    
