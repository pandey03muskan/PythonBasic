def SumDigit(i):
        sum=0
        while(i>0):
           rem=i%10
           sum=sum+rem
           i=i//10
        return sum
list=[125,238,276,3471,834267]
newlist=[SumDigit(n) for n in list if(n%2!=0)]
print(newlist)