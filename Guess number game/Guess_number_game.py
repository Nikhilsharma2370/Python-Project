import random
randomno = random.randint(1,100 )

print(randomno)
guess = None
a = 0
while guess != randomno:
    guess = int(input("Enter your Number in 1 to 100\n"))
    a += 1
    if guess == randomno:
        print("this is right")
    else:
        if guess>randomno:
            print("greater than random no please enter small no")
        else:
            print("lesser than random no please enter larger no")
            
        
print(f"Your guess number{a}")

with open("hiscore","r") as f:
    hi = f.read()
if hi=="":
    with open("hiscore","w") as f:
        m = f.write(str(a))
elif a<int(hi):
    print(f"your are broken the pervious high score {hi}")

    with open("hiscore","w"  ) as f:
        f.write(str(a))
    print(f"your high score{a}")