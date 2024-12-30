#Write a program that takes two numbers and prints out the result of integer division and theremainder.
x=[]
for i in range(2):
   x.append(int(input(f"Enter number {i+1}:")))
   
print(f"division result:{x[0]/x[1]}\nreminder result:{x[0]%x[1]}") 