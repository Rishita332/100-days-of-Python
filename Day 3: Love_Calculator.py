print("Welcome to the Love Calculator")
name1=input("What is you name? ")
name2=input("What is their name? ")
name1.lower()
name2.lower()
a=0
b=0
for l in 'true':
   a+= name1.count(l)+ name2.count(l)

for l in 'love':
    b+= name1.count(l)+ name2.count(l)
    
score=a*10+b   
if score<10 and score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")    
else:
    print("Your score is", score)    
    

 


