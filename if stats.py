#do soem code only if some condition is satisfied
#else do something else

age = int(input("enter your age:"))
if age>=100:
    print("you are too old!")

elif age >=18:
    print("you are an adult")
elif age <0:
    print("you haven't been born yet")      
else:
    print("you are a minor")
    
online = True

if online:
    print("the user is online")
else: 
    print("the user is offline")
