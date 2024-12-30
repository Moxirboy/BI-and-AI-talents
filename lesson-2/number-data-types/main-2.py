#Write a Python file that asks for three numbers and outputs the largest and smallest.
x=[]
for i in range(3):
    y=int(input(f"enter number{i}:"))
    x.append(y)
    
print(f"max:{max(x)}\nmin:{min(x)}")