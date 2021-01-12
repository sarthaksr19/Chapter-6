text = input("enter the text\n")

if("make a lot of money" in text):
    spam = True
    # print("this text contain spam")
elif("buy now" in text):
    spam = True
    # print("this text contain spam")

elif("click this" in text):
    spam = True
    # print("this text contain spam")

elif("suscribe this" in text):
    spam = True
    # print("this text contain spam")

else:
    spam = False
    # print("given text has no spam")

## printing the statement through spam boolean value thus it takes less time to wrote our code and make our program shorts.

if(spam):
    print("this text contain spam")
else:
    proint("given text has no spam")