print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name_1= name1.lower()
lower_case_name_2= name2.lower()

T=lower_case_name_1.count("t")+ lower_case_name_2.count("t")
R=lower_case_name_1.count("r")+ lower_case_name_2.count("r")
U=lower_case_name_1.count("u")+ lower_case_name_2.count("u")
E=lower_case_name_1.count("e")+ lower_case_name_2.count("e")

result_1=int(T+R+U+E)

L=lower_case_name_1.count("l")+lower_case_name_2.count("l")
O=lower_case_name_1.count("o")+lower_case_name_2.count("o")
V=lower_case_name_1.count("v")+lower_case_name_2.count("v")
E=lower_case_name_1.count("e")+lower_case_name_2.count("e")

result_2=int(L+O+V+E)

final_result=str(result_1)+str(result_2)

if int(final_result)>40 and int(final_result)<50:
    print(f"Your score is {int(final_result)}, you are alright together.")
elif int(final_result)<10 or int(final_result)>90:
    print(f"Your score is {final_result}, you go together like coke and mentos.")
else:
    print(f"Your score is {int(final_result)}.")
