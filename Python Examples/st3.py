name = input ("Enter your name: ")

percentage = float (input("Enter your percentage: "))

if percentage < 40 and percentage > 0:
    print (f"Welcome {name} Sir!, please lead our country")
elif percentage > 40 and percentage <=50:
    print (f"Welcome {name} to politics Sir!")
elif percentage > 50 and percentage <=60:
    print (f"Welcome {name} to sabzi mandi")
elif percentage > 60 and percentage <=70:
    print (f"Welcome {name} to homeless and jobless union of beroozgar people")
elif percentage > 70 and percentage <=80:
    print (f"Welcome {name} to private 9-5 job")    
elif percentage > 80 and percentage <=100:
    print (f"Welcome {name} to Teachers union in private school")
else:
    print ("Insan k bache banoo")
                    