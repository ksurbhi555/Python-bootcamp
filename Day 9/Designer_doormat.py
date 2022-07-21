n=int(input(""))
m=int(input("")) 
y=round((m-3)/2)
s=round((m-7)/2)


verticle = (range(1,n,2))
horizontal = (range((y),0,-3))
for x, j in zip(verticle, horizontal):
    print("-"*j + ".|."*x + "-"*j)

print("-"*s + "WELCOME" + "-"*s)


vert = (range(n-2,-1,-2))
hori = (range(3,(y+3),3))
for a, b in zip(vert, hori):
    print("-"*b + ".|."*a + "-"*b)
        
