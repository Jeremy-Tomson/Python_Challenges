TheTime = int(input("What time is it now?"))
test = input("Is it AM or PM?")
if test in ["pm", "PM"]:
    if TheTime == ["1200"]:
        NewTime = TheTime - 1200
        print("The time in 12 hour is %d" % NewTime)
    else:
        NewTime = TheTime + 1200
        print("The time in 24 hour is %d" % NewTime)
if test in ["am", "AM"]:
    NewTime = TheTime
    print("The time in 24 hour is %d" % NewTime)
