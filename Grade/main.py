#Yenesis Rabelo Grade SkillPractice

def determine_grade():
    # asking the user for their grade percentage
    percentage = float(input("Enter your grade percentage: "))
    
    # checking the grade percentage and output the corresponding letter grade
    if percentage >= 90:
        print("You have an A.")
    elif percentage >= 80:
        print("You have a B.")
    elif percentage >= 70:
        print("You have a C.")
    elif percentage >= 60:
        print("You have a D.")
    else:
        print("You have an F.")
