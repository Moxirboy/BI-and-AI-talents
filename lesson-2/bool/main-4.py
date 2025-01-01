x = [0,0,0]
y = False
for i in range(3):
    a = int(input(f"enter number {i+1}: "))
    if a in x :
        y = True
    x[i] = a
if y:
    print("there is dublicate")
else:
    print("there is not dublicate")
