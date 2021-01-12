userName = input("enter username\n")

length = len(userName)  #using len() fuction to determine length

if(length >= 10):
    print("given username is above 10 character")
else:
    print("given username is less than 10 character")