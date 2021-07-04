def game():
    return int(input("Enter your score"))

score = game()

with open("jscore","r") as f:
    n = f.read()

if n=="":
    with open("jscore","w") as f:
        m = f.write(str(score))
elif int(n)<score:
    with open("jscore","w") as f:
        m = f.write(str(score))
else:
    print(f"previous score is high Previous score{n}")        


with open("jscore","r") as f:
    j = f.read()

print(f"high score  {j}")


