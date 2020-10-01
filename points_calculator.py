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
    age_points = 0

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
    

#if ielts choose this option; if toefl choose this option and if pte, choose this option.
    print("Applicants can get upto 20 more points based on their English speaking abilities.")
    english = input("How's your English language ability? (1.Superior/2.Proficient/3.Competent)")

    english_points = 0
    if english.casefold() == "Superior" or "1":
        english_points = 20
        print(("Congratulations! You have received {} more points.").format(english_points))
    elif english.casefold() == "Proficient" or "2":
        english_points = 15
        print(("Congratulations! You have received {} more points.").format(english_points))
    elif english.casefold() == "Competent" or "3":
        english_points = 10
        print(("Congratulations! You have received {} more points.").format(english_points))
    

#Skilled Employment in Last 10 years:
    print("Additionally, you can claim upto 20 more points through your skilled employment in last 10 years.")
    employment = input("How long were you employed in your skill-nominated occupation? (in years)")
    employment =int(employment)

    employment_points = 0
    if 0<employment<1:
        employment_points = 0
        print(("You have received {} points.").format(employment_points))
    elif 1<employment<3:
        employment_points = 5
        print(("Congratulations! You have received {} more points.").format(employment_points))
    elif 3<employment<5:
        employment_points = 10
        print(("Congratulations! You have received {} more points.").format(employment_points))
    elif 5<employment<8:
        employment_points = 15
        print(("Congratulations! You have received {} more points.").format(employment_points))
    elif 8<employment<10:
        employment_points = 20
        print(("Congratulations! You have received {} more points.").format(employment_points))
    


#Qualifications
    print("Another Criteria for gaining points is through educational qualifications.")
    qualification = input("What is your Highest degree of qualifications? Please choose between: "+
                          "\n1. Doctorate \n2. Master's Degree \n3. Bachelor's Degree \n4. Diploma")

    qualification_points = 0
    if qualification.casefold()== "Doctorate" or "1":
        qualification_points =20
        print(("Excellent! You have received {} more points.").format(qualification_points))
    elif qualification.casefold()== "Bachelor's Degree" or "3":
        qualification_points = 15
        print(("Excellent! You have received {} more points.").format(qualification_points))
    elif qualification.casefold()== "Master's Degree" or "2":
        qualification_points = 15
        print(("Excellent! You have received {} more points.").format(qualification_points))
    elif qualification.casefold()== "Diploma" or "4":
        qualification_points = 10
        print(("Excellent! You have received {} more points.").format(qualification_points))
    

#Recog. University = 10
    recognition = input("Do you have at least one degree (Diploma/Bachelor/trade qualifications)" +
          "from an Australian educational institutions? (Yes/No)")
    recognition_points = 0
    if recognition.casefold() == "yes":
        recognition_points = 10
        print("Awesome! 10 more points at your score.")
    elif recognition.casefold() == "no":
        recognition_points = 0
        print("Let's examine other fields")
    

#Professioinal Year
    print("You can also maximize your Points via Professional Year in Australia.")
    py = input("Have you completed your professional year in Australia? (Yes/No)")
    py_points = 0
    if py.casefold() == "yes":
        py_points = 5
        print("Well done! You have 5 more points.")
    elif py.casefold() == "no":
        py_points = 0
        print("Let's examine other fields")
    


#NAATI
    print("Australian PR system gets you point not only for English language" +
          " but also for your local language translation ability.")
    naati = input("Do you hold a recognised qualification in a credentialled community language ? (Yes/No)")

    naati_points = 0
    if naati.casefold() == "yes":
        naati_points = 5
        print("Well done! You have 5 more points.")
    elif naati.casefold() == "no":
        naati_points = 0
        print("Let's examine other fields")
    

#Study in Regional Australia
    regional = input("Do you have at least one degree obtained while living and studying in Regional Australia? (Yes/No)")

    regional_points = 0
    if regional.casefold() == "yes":
        regional_points = 5
        print("Awesome! 5 more points at your score.")
    if regional.casefold() == "no":
        regional_points = 0
        print("Let's examine other fields")
    

#Partner Assessment
    print("You can also claim upto 10 points through your partner's skills.")
    partner = input("Does your partner have competent English and Skilled occupation? (Yes/No)")

    partner_points = 0
    if partner.casefold() == "yes":
        partner_points = 10
        print(("Excellent! You have received {} more points.").format(partner_points))
    if partner.casefold() == "no":
        partner_points = 5
        print(("Excellent! You have received {} more points.").format(partner_points))
    

#Result
    Total_score = age_points + english_points + employment_points + py_points + naati_points + regional_points
    print(("Your total score is {}").format(Total_score))
    if 65<=Total_score<=70:
        print("Processing time for your invitation may reach over a year.")
    elif 75<=Total_score<=85:
        print("Processing time for your invitation may reach about 8 to 9 months")
    elif 85<=Total_score<=95:
        print("Processing time for your invitation may reach about 1 to 2 months.")
    exit()
    
