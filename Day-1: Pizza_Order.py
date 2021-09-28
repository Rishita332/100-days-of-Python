print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M, L :  ")
pep=input("Do you want peproni? Y or N : ")
cheese=input("Do you want extra cheese? Y or N : ")
bill=0
if size=='S':
    bill+=15
    if pep=='Y':
        bill+=2
elif size=='M':
    bill+=20
    if pep=='Y':
        bill+=3
else:
    bill+=25
    if pep=='Y':
        bill+=3
if cheese=='Y':
    bill+=1
print("Total Bill= $",bill)    



    
