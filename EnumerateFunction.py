# enumerate function gives you the index with its respective values

# it prints a tuple of index and value pair
marks=[12,56,32,98,12,45,1,4]
for v in enumerate(marks):
    print(v)
    
#you can unpack the index and values 
for index,mark in enumerate(marks):
    print(marks[index],"with index")
    print(mark,"with value")

#Change start of the index
for index,mark in enumerate(marks,start=1):
    print(marks[index])