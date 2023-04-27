name=input("Please Enter your name......")
print("Here the characters of your name.....")
for name in name:
    print(name,end=",")
    
#WITH RANGE FUNCTION
#with only one argument
for number in range(5):
    print(number)
#with range from a number to a specific number
for number in range(0,5):
    print(number)
#with step argument [here third argument is step argument which defines by how many step go ahead at one time]
for number in range(0,9,2):
    print(number)