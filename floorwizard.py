# converts between us and european floors
while True:
    case=input("Which would you like to convert from? (us/eur)")
    if case=="us":
        try:
            us=int(input("Enter US floor"))
            eur=us-1
            print("European floor",eur)
            break
        except:
            print("Please enter an integer!")
            continue
    elif case=="eur":
        try:
            eur=int(input("Enter European floor"))
            us=eur+1
            print("US floor", us)
            break
        except:
            print("Please enter an integer!")
            continue
    else:
        #if case is not one of the two valid options
        print("Please try again and enter a valid choice!")
        continue
