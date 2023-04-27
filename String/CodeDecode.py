message=input()
listmsg=[]
newstr=''
print("-------Encoding of your name is-------\n")
if(len(message)>2):
    for i in message:
     listmsg.append(i)
    newstr=newstr+'abc'
    newstr=newstr+"".join(listmsg[1:])
    newstr=newstr+listmsg[0]
    newstr=newstr+'xyz'
    print(newstr)
else:
    print(message[::-1])
print("------Decoding of encoded name------\n")
removeUnnecessary=newstr[3:-4]
decodedmsg=newstr[-4]
print(decodedmsg+removeUnnecessary)