a="Muskan Pandey"
#POSITIVE SLICING
print(a[0:5])
print(a[:])
print(a[2:])
print(a[:11])

#NEGATIVE SLICING
print(a[0:-1]) # it means a[0:len(a)-1]==>a[0:13-1]
print(a[0:12]) #it is same as like line 3
print(a[-4:-1]) #a[len(a)-4:len(a)-1]==>a[9:12]
print(a[9:12])

#QUIZ
nm="Harry"
print(nm[-4:-2])
print(nm[1:3])