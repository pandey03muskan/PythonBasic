questions=[
    ["What is my name",'Muskan Pandey','Vijeta Mishra','Shivani Pandey','Mansi Srivastava'],
    ["Who I am",'Developer','problem solver','Student','All'],
    ["I am currently living in",'MMM','','Ayodhya','Kanpur','woiueiuisd']
    ]
level=[1000,2000,5000]
print(f"Your Question for rupees {level[0]}")
for i in range(len(questions)):
    print(questions[i][0])
    print(f"[a]. {questions[i][1]}       [b]. {questions[i][2]}")
    print(f"[c]. {questions[i][3]}       [d]. {questions[i][4]} ")
    reply=int(input("Enter your answer from 1 to 4 =>"))
    if(questions[i][i+1]==questions[i][reply]):
        print(f"Correct Answer, you won Rs.{level[i]}\n")
    else:
        print("Wrong Answer")
    if(len(level)-1>i):
      print(f"Next question for rupees {level[i+1]}")
    