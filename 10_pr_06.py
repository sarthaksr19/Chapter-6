studentMarks = int(input("enter student total marks\n"))

if(studentMarks<=100 and studentMarks>90):
    print("grade-Excellent")

elif(studentMarks<=89 and studentMarks>80):
    print("grade-A")
elif(studentMarks<=79 and studentMarks>70):
    Print("grade-B")

elif(studentMarks<=69 and studentMarks>60):
    print("grade-C")

elif(studentMarks<=59 and studentMarks>50):
    print("grade-D")

elif(studentMarks<=49):
    print("grade-F")

else:
    print("enter the valid total marks")
