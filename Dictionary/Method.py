ep1={122:45,123:89,567:69,670:69}
ep2={222:62,566:90}

# HOW TO UPDATE=>updates ep1 dict with the ep2 dict
ep1.update(ep2)
print(ep1)

# CLEAR FUNCTION DELETE ALL THE ELEMENTS OF THE DICTONARY
ep2.clear()
print(ep2)

# POP REMOVES VALUE BY KEY, IF KEY IS NOT PRESENT THEN IT GIVES NONE
ep1.pop(123)
print(ep1)

# POPITEM IS USED TO REMOVE LAST ELEMENT FROM DICT
ep1.popitem()
print(ep1)

#DEL IS NOT A FUNCTION=>if you want to delete all the items with dictionary then use del 
del ep2
# print(ep2) #NameError: name 'ep2' is not defined. Did you mean: 'ep1'?

