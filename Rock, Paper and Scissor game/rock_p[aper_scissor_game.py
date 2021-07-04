import random
#rock paper and scissors
def gamewin(comp,you):
    
    if comp == you:
        return None
    
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
            
print("compu+ter choose randomly rock(r) , paper(p) and scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp ='r'
elif randNo == 2:
    comp ='p'
elif randNo == 3:
    comp ='s'

you=input("your turn choose rock(r) , paper(p) and scissor(s)?\n")
a=gamewin(comp,you)

if comp == 'r':
    print(f"Computer choose  {comp}(Rock)")
elif comp == 'p':
    print(f"Computer choose  {comp}(Paper)")
else:
    print(f"Computer choose  {comp}(Scissor)")

if you == 'r':
    print(f"Your choose  {you}(Rock)")
elif you == 'p':
    print(f"Your choose  {you}(Paper)")
else:
    print(f"Your choose  {you}(Scissor)")





if a == None:
    print("Match is Try")
elif a:
    print("Won")
else:
    print("Lose")
