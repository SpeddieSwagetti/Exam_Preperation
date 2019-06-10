"""Name: Mitchell Marks
Date started: 06/06/2019
Brief Description: Program to check if a person can vote. They must be 18 or older, and they must be enrolled"""

VOTE_AGE = 18
enrollment = False
enrollment_changer = ""
current_age = 0

while current_age <= 0:
    try:
        current_age = int(input("Please enter your age:"))
        if current_age <= 0:
            print("Number must be greater than 0!")
    except ValueError:
        print("Must be a number:")

while enrollment_changer != "Y" and enrollment_changer != "y" and enrollment_changer != "N" and enrollment_changer != "n":
    enrollment_changer = input("Are you enrolled? ")
    if enrollment_changer == "Y" or enrollment_changer == "y":
        enrollment = True
    else:
        enrollment = False

if current_age >= VOTE_AGE:
    if enrollment is True:
        print("You are elligable to vote!")
    else:
        print("You are old enough to vote, but not enrolled")
else:
    print("Sorry, you are not old enough to vote")
