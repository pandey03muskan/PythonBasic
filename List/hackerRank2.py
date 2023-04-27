n=int(input())
list=[]
li1=[-1,1,-7,-8]
li2=[-10,-8,-5,-2]
li3=[0,9,7,-1]
li4=[4,4,-2,1]
sum1=0
sum2=0
list.append(li1)
list.append(li2)
list.append(li3)
list.append(li4)
for i in range(len(list)):
    for j in range(len(list)):
        if(i==j):
            sum1=sum1+list[i][j]
        if((i==0+i and j==n-i-1)):
            sum2=sum2+list[i][j]
print(sum1-sum2)    