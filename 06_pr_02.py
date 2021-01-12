s1 = int(input("enter math marks\n"))
s2 = int(input("enter physics mark\n"))
s3 = int(input("enter chemistry marks\n"))
totalMarks = (s1+s2+s3)/300*100

# if(totalMarks>=40 or s1>=33):
#     print("student is passed in maths")
if(s1>=33):
    print("student is passed in maths",s1)
else:
    print("student is failed in maths",s1)

if(s2>=33):
    print("student is passed in physics ",s2)
else:
    print("student is failed in physics",s2)

if(s3>=33):
    print("student is passed in chemistry ",s3)
else:
    print("student is failed in chemistry",s3)
if(totalMarks>=40):
    print("total aggregate of 3 subjects",totalMarks, "PASS")  
else:
    print("failed to clear 40% ",totalMarks ,"FAILED!")
# print("the total percentage of the student",totalMarks)