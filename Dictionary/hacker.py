
from collections import Counter
t=int(input())
ShoeNo=list(map(int,input().split()))
dict=Counter(ShoeNo)
total=0
n=int(input())
for i in range(n):
    size,amount=map(int,input().split())
    if(dict[size]>0):
      if size in dict:
        total=total+amount
        dict[size]=dict[size]-1  
print(total)

    
  