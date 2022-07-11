numbers=input("Enter your class scores ").split(",")
for n in range(0,len(numbers)):
  numbers[n]=int(numbers[n])


total_scores=sum(numbers)
print(f"Total scores are:{ total_scores}")

total_students=0
for students in numbers:
  total_students=(total_students)+1
print(f"Total number of students are: { total_students}")

Average_score=round(total_scores/total_students)
print(f"The average score is: { Average_score}")

maximum=max(numbers)
print(f"Maximum marks obtained: {maximum}")

minimum=min(numbers)
print(f"Minimum marks obtained:{ minimum}")
