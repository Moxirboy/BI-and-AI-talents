vowels = ["a","e","i","o","u"]
x = input("Enter your sentence: ")
for v in vowels:
    x = x.replace(v,"*")
print(f"replaced new string: ${x}")


