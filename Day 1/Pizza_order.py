print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size=="S":
    bill=15
    if add_pepperoni=="Y":
       bill+=2
    if extra_cheese=="Y":
       bill+=1

    print(f"Your final bill is: ${bill}.")


bill_n=0
if size=="M":
    bill_n=20
    if add_pepperoni=="Y":
       bill_n+=3
    if extra_cheese=="Y":
       bill_n+=1
    
    print(f"Your final bill is: ${bill_n}.")


bill_m=0
if size=="L":
    bill_m=25
    if add_pepperoni=="Y":
         bill_m+=3
    if extra_cheese=="Y":
        bill_m+=1
    
    print(f"Your final bill is: ${bill_m}.")
