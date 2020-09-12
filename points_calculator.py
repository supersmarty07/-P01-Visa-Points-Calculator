state = ["NSW","VIC","TAS", "QLD", "NT", "SA", "WA","ACT"]

#Input name, create response to further Customer's inquiries or exit the program

while True:
    name = input("My name is Abacus, your friendly Visa Helper." +
                 " What's your name? ").strip().capitalize()
    print(("Hi {}. How are you doing today?").format(name))
    input()
    aws = "Awesome!"
    print(aws)
    calculate_today = input("Would you like me to" +
                            " calculate your PR Points today?: ")
    start = calculate_today.strip().lower()
    if start == "yes" or  start == "ok" or start =="sure":
        print(aws + " Let's get started.")
        print("This is a general Point Calculator" +
              " for Temporary Residents of Australia." +
              "\nYour nomination is subjected to be granted based"
              " on the criteria of state you live in." +
              "\nEach state has its own demand of labour market." +
              "\nYou're more likely to get your Permanent Residency if you" +
              " have the same occupation as listed in the demand market of the " +
              "state.")
    else:
        trial= ("I can only assist you to calculate your PR points.\nPlease talk " +
                "to Customer Service for further assistance." +" Have a good day {}. ")
        print(trial.format(name))
        break


#If unclear, choose this option to get further reponse and continue with the program

    print("Are you clear so far? ")
    clear = input().strip().lower()
    if clear == "yes" or clear == "sure" :
            print("This test is specialised for applicants of Permanent Residency "
              + "in NSW. ")
    else:
        print("For example: To get PR in NSW, the applicant has to fulfill many " +
              "criteria. He could be rejected even though he has 85 points. " +
              "\nWhereas NT may grant you PR relatively easily inspecting less " +
              "criteria and points as less as 65. Therefore, each state has its " +
              "own criteria for the applicants. \nThe hardships of " +
              "these applications depends on these criteria set by the State " +
              "Government.")
        
#Current Place of Residence
        
    print("That being said, let's get right into it.")
    living = input ("What state do you live in? ")
    city = living.strip().upper()
    if city in state:
            print (("{} is an amazing place. ").format(city))
    else:
            print("I can't wait to see you in Australia.")

    print("Let's get started with your age. \nIn Australia, you need to be below " +
              "45 to apply for Permanent Residency. " +
              "\nYou can get some points based on your age.")

    #Calculate age from date
    import datetime

    dob = input("Please input your Date of Birth in ddmmyyyy: ")

    birth_year = int(dob[4:])
    birth_month = int(dob[2:4])
    birth_day = int(dob[0:2])

    from datetime import datetime
    today = datetime.today().strftime('%Y,%m,%d')

    today_year = int(today[0:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])

    age = int((today_year - birth_year) + (today_month - birth_month)/12 + (today_day - birth_day)/365.25)
    

    if 18<age<25:
        age_points = 25
        print(("Congratulations! You have received {} points.").format(age_points))
    elif 25<age<32:
        age_points = 30
        print(("Congratulations! You have received {} points.").format(age_points))
    elif 33<age<39:
        age_points = 25
        print(("Congratulations! You have received {} points.").format(age_points))
    elif 40<age<44:
        age_points = 15
        print(("Congratulations! You have received {} points.").format(age_points))
    else:
        print("Sorry! You are not eligible./nPlease Contact Customer Service for further inquiries.")

#if ielts choose this option; if toefl choose this option and if pte, choose this option.
    print("Applicants can get upto 20 more points based on their English speaking abilities.")
    test = input




