n = int(input("Check this number: "))

def prime_checker(number=n):
    check=True
    for i in range(2,n):
        if n%i==0:
            check=False
    
    if check==True:
        print("It's a prime number.")
    
    else:
        print("It's not a prime number.")


prime_checker()
            
