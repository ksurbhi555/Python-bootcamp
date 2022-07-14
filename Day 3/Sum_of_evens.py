uptil=(input("Sum of even numbers upto: "))
last=int(uptil)+(1)
total=0
for numbers in range(0,(last),2):
  total=total+numbers
print(f"The answer is: {total}")
