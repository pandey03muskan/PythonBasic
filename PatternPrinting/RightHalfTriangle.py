n=int(input())
for i in range(n):
    j=n-i-1
    k=j
    while(j>0):
        print(" ",end='')
        j=j-1
    while(k<n):
        print("*",end='')
        k=k+1
    print()
    