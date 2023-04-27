
N=int(input())
s=set(map(int,input().split()))
print(s)
for i in range(N):
    Clist=[]
    command=input()
    for j in command:
        Clist.append(j)
    if(Clist[0]=='p'):
        s.pop()
    elif(Clist[0]=='r'):
        s.remove(int(Clist[-1]))
    elif(Clist[0]=='d'):
        s.discard(int(Clist[-1]))
sum=0
for i in s:
    sum=sum+i
print(sum)