a=[1,3,6,1,3,6]
#append the element at the end of the list
a.append(9)
print(a)
#used to sort the list for descending order we can use reverse=True property within the function argument
a.sort()
print(a)
a.sort(reverse=True)
print(a)
#used to reverse the list
a.reverse()
print(a)
#to counts the occurance of specific symbol in the list
print(a.count(1))
#to make a copy of the list
m=a.copy()
m[0]="muskan"
print(m)
print(a)
#append element at specific position
a.insert(1,"pandey")
print(a)
#merge two lists
s=["muskan","vijeta","friend"]
a.extend(s)
print(a)

