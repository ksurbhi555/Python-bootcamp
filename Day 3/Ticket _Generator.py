print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 10
        print("Child ticket 10 Rs.")

    elif age <= 18:
        bill = 20
        print("Youth ticket is 20 Rs.")

    elif age >= 45 and age <= 55:
        print("Everything gonna be okay. Have a free ride on us.")

    else:
        bill = 30
        print("Adult ticket is 30 Rs.")

    want_photo = input("Want photo? Y or N?")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is Rs {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")
