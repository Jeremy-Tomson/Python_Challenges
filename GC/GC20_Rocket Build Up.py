Hours = 51
Days = 0
while Hours > 24:
    Hours = Hours - 24
    days = Days +1
    if Hours < 24:
       FinalTime = 2 + Hours
       print("The time that the rocket will be ready is at %s pm." % FinalTime)
       print(Days)
