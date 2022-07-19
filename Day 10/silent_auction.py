from replit import clear

from art import logo
print(logo)

dict1={}
Repeat=True

def function(dict1):
    highest_bid = 0
    winner=""
    for person in dict1:
        amount=dict1[person]
        if int(amount) > highest_bid:
            highest_bid=int(amount)
            winner=person
    print(f"The winner is {winner} with bid: {highest_bid}")
            
while Repeat:
    name=input("What is your name? ")
    bid=input("What is the bid amount")
    
    dict1[name]=(bid)

    ques=input("if tou wanna repeat type'yes' else type 'no'.")
    if ques=='no':
        Repeat=False
        function(dict1)
    elif ques=='yes':
        clear()
