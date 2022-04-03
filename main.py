import time
from graph_class import graph
from tqdm import tqdm

print("COVID-19 Diagnosis: Version 1.0")

print(
    "\n-------------------------------------------------------------------------------------------------------------------")

def welcome():
    print("\nWelcome to COVID-19 Diagnosis!")
    print("I will be your personal guide related to the on-going pandemic, COVID-19")

def error():
    print("Sorry, but I did not quite understand what you have typed. Please press the corresponding letters for your response.")

def question():
    res = input(
        "\nWhat are you looking for today? \n[a] COVID-19 Cases \n[b] Diagnosis \n[c] Tips on staying safe \n> ")
    res = res.lower()
    if res == "a":
        return cases()
    elif res == "b":
        return diagnosis()
    elif res == "c":
        return tips()
    else:
        error()
        return question()

def cases():
    res = input("\nWhat kind of case would you like to look over? \n[a] Total COVID-19 Cases \n[b] New COVID-19 Cases \n> ")
    res.lower()
    if res == "a":
        return totalCase()
    elif res == "b":
        return newCase()
    else:
        error()
        return cases()

def totalCase():
    print("The graphical data for China, France, Italy, South Korea, Spain, United States has been recorded.")
    l = ["China", "France", "Italy", "South Korea", "Spain", "United States"]
    c  = ["China", "France", "Italy", "South Korea", "Spain", "United States"]
    graph.totalCases(l,c)

def newCase():
    print("The graphical data for China, France, Italy, South Korea, Spain, United States has been recorded.")
    l = ["China", "France", "Italy", "South Korea", "Spain", "United States"]
    c  = ["China", "France", "Italy", "South Korea", "Spain", "United States"]
    graph.newCases(l,c)

def diagnosis():
    print("Please answer the following questions in order to check for signs of COVID-19.")
    print(
    "\n-------------------------------------------------------------------------------------------------------------------\n")
    for i in tqdm(range(5)):
        time.sleep(1)
    score = 0
    q1 = input("Do you feel headaches often? \n[a] Yes \n[b] No \n> ")
    if q1 == "a":
        score += 1
    elif q1 == "b":
        score  += 0
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()
    q2 = input("Have you been feeling tired lately? \n[a] Yes \n[b] No \n> ")
    if q2 == "a":
        score += 1
    elif q2 == "b":
        score  += 0
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()
    q3 = input("Have you have been coughing more often recently? \n[a] Yes \n[b] No \n> ")
    if q3 == "a":
        score += 1
    elif q3 == "b":
        score  += 0
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()
    q4 = input("Are you able to smell and taste food normally? \n[a] Yes \n[b] No \n> ")
    if q4 == "a":
        score += 0
    elif q4 == "b":
        score  += 1
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()
    q5 = input("Does your throat feel soar? \n[a] Yes \n[b] No \n> ")
    if q5 == "a":
        score += 1
    elif q5 == "b":
        score  += 0
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()

    if score >= 3:
        print("You are highly suggested to take a home test kit or a PCR test.\n")
    elif score < 3:
        print("You may take a home test kit or PCR test when your symptoms get worse.\n")
    else:
        error()
        print("Restarting diagnosis...")
        time.sleep(2)
        return diagnosis()

    time.sleep(1)
    print("The given questions contained the most common symptoms of getting COVID-19. Below is the whole list of possible symptoms that can rise up during the infection of COVID-19.")
    time.sleep(1)
    print("""
Most common symptoms:
 - fever
 - cough
 - tiredness
 - loss of taste or smell
Less common symptoms:
 - sore throat
 - headache
 - aches and pains
 - diarrhoea
 - a rash on skin, or discolouration of fingers or toes
 - red or irritated eyes
Serious symptoms:
 - difficulty breathing or shortness of breath
 - loss of speech or mobility, or confusion
 - chest pain
    """)

def tips():
    mask = [
        "Wear a mask with the best fit, protection, and comfort for you.",
        "Even when staying indoors in a public area, wearing a mask is highly suggested."
    ]
    crowd = [
        "If indoors, bring in fresh air by opening windows and doors, if possible.",
        "Avoid crowded placess and indoor spaces that do not have fresh air."
    ]
    clean = [
        "Always remember to wash your hand in all instances.",
        "If soap and water is not accessible, use a hand sanitizer with >60% alcohol",
        "Avoid touching your eye, nose, and mouth with unwashed hands."
    ]
    disinfect = [
        "Clean surfaces that get touched a lot regularly or after you have visitors in your home.",
        "If someone is sick of has tested positive for COVID-19. disinfect frequently the surfaces touched."
    ]
    print("\nWear a mask!: ")
    for i in enumerate(mask, start=1):
        print("\t", *i, sep=". ")
    print("\nAvoid poorly ventilated spaces and crowds!: ")
    for ii in enumerate(crowd, start=1):
        print("\t", *ii, sep=". ")
    print("\nWash your hands often!: ")
    for iii in enumerate(clean, start=1):
        print("\t", *iii, sep=". ")
    print("\nClean and disinfect!: ")
    for iv in enumerate(disinfect, start=1):
        print("\t", *iv, sep=". ")

def ending():
    res = input(
        "\nIs there anything else that you would like to check? \n[a] COVID-19 Cases \n[b] Diagnosis \n[c] Tips on staying safe \n[d] End \n> ")
    res.lower()
    if res == "a":
        return cases()
    elif res == "b":
        return diagnosis()
    elif res == "c":
        return tips()
    elif res == "d":
        print("Thank you for sticking with COVID-19 Diagnosis for today! See you next time~")
        time.sleep(2)
        exit()
    else:
        error()
        return ending()

welcome()
question()
while True:
    ending()