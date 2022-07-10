import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

#counts the total names in list
num_items = len(names)

#picks up random no.
random_choice = random.randint(0, num_items-1)

#connects_random_no._with list
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay } will pay.")
