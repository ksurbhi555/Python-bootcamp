from tabulate import tabulate
name=input("What is your name? ")
standard=(input("Your class? "))

maths=input("How much did you scored in maths? ") 
sci=input("How much did you scored in science? ")  
sst=input("How much did you scored in SST? ") 
hin=input("How much did you scored in hindi? ") 
eng=input("How much did you scored in english? ") 
bt=input("How much did you scored in biotech? ") 
print(".................................................................................")
txt = "SCORE CARD"

x = txt.center(90)

print(x)
print(".................................................................................")
print(f"NAME:{name}")
print(f"CLASS:{standard}")

mydata = [
    ["Maths",(maths),"80"],
    ["Science",(sci),"80"],
    ["SST",(sst),"80" ],
    ["Hindi", (hin),"80"],
    ["English",(eng),"80"],
    ["Biotech",(bt),"80"]
    
]
 
head = ["Subject", "Scores Obtained","Max Scores"]
 
print(tabulate(mydata, headers=head, tablefmt="grid"))

total=int(maths)+int(sci)+int(sst)+int(hin)+int(eng)+int(bt)
print(f"Total marks obtained: {total}")
print("Maximum marks: 480")

percent=round((total)/4.8,2)
print(f"PERCENTAGE OBTAINED: {percent}%")

print(".................................................................................")
