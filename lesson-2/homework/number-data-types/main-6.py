#Create a program that accepts a number and returns the last digit of that number.


#With operation integer
x=int(input("Enter number:"))
print("List of digits:", end=" ")
while x>0:
    print(f"{x%10}",end=" ")
    x=int(x/10)

# #With string
x=input("Enter Number: ")
print("List of digits:", end=" ")
print(' '.join([str(i) for i in x]))
