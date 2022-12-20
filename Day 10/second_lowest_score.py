total_students=int(input("total students: "))
#................................................
names=[]
scores=[]
for x in range(total_students):
 name_input=input("name: ")
 score_input=input("score: ")
 print("\n")   
 names.append(name_input)
 scores.append(score_input)

print(f"original scores list:{scores}")
print(f"original names list:{names}")
    
for n in range(len(scores)):
    scores[n]=float(scores[n])

data=list(zip(names,scores))

temp = []

for x in scores:
    if x not in temp:
        temp. append(x)
scores = temp
print(f"temp with score:{scores}")

min=1000
for x in scores:
    if x<= min:
        min = x
scores.remove(min)
scores.sort()
print(f"scores list after lowest removed and sorted {scores}")

list=[]
sec_min=1000
for x in scores:
    if x<= sec_min:
        sec_min=x
list.append(sec_min)
#print(f"second lowest in list {list}")

result=[]
for x,y in data:
    if y==sec_min:
       result.append(x)
       result.sort()

for i in result:
    print(f"{i} scored second lowest.")
