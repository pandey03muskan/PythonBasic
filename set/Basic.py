#how to create empty set   s={}  # no this is synatx for dict so,let's see
s1=set()
s1={1,2,4,2,5,5,6}
s2={3,4,7}

#set always contains unique values/do not allow duplicates
print(s1) #{1,2,4,5,6}

#set can contain multiple datatype values
s3={"muskan",1,4}
print(s3)

#sets are unorderded
s4={'muskan',1,3,'pandey',8,'h'}
print(s4)#{1, 3, 8, 'h', 'muskan', 'pandey'} 1st time
         #{1, 'h', 3, 8, 'muskan', 'pandey'} next time and so on
#immutable
