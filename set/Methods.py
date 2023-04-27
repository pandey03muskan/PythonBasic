#UNION=>same as union of set in maths
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #{1, 2, 3, 5, 6, 7}

#INTERSECTION=>print common values
print(s1.intersection(s2))#{6}

#SYMMETRIC_DIFFERENCE=>removes common values
print(s1.symmetric_difference(s2))#{1, 2, 3, 5, 7}

#DIFFERENCE=>exist in 1st not in 2nd
print(s1.difference(s2))#{1, 2, 5}

#UPDATE=>update function updates a set with the value of another set 
print(s1)#{1, 2, 5, 6}
s1.update(s2)
print(s1)#{1, 2, 3, 5, 6, 7}

#ISDISJOINT=>returns boolean value True/False
print(s1.isdisjoint(s2))#False

#ISSUPERSET=>returns boolean values True/False
print(s1.issuperset(s2))#True

#ISSUBSET
print(s1.issubset(s2))#False

#remove/discard
s1.remove(2)
print(s1)#{1, 3, 5, 6, 7}
s1.discard(2)
print(s1)#{1, 3, 5, 6, 7} does not raise error whenever key is not present
'''again'''
s1.discard(1)
print(s1)#{3, 5, 6, 7}
'''s1.remove(1)
 print(s1)#KeyError: 1 it returns error if key is not present'''

#del
print(s2)#{3, 6, 7}
del s2 
'''it delete the complete set
 print(s2) #NameError: name 's2' is not defined. Did you mean: 's1'? because s2 does not exist anymore'''

#pop
print(s1.pop()) # 3 pop random element from set