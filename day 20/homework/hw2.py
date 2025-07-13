str1=input("enter a day of the week: ")
match str1:
    case "Monday":
        print("კვირის დასაწყისი")
    case "Tuesday"|"Wednesday"|"Thursday":
        print("შუა კვირა")
    case "Friday":
        print("შაბათ-კვირას ახლოს")
    case "Saturday"|"Sunday":
        print("შაბათ-კვირა")
    case _ :
        print("არასწორი დღე")