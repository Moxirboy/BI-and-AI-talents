#Write a program that asks the user for a sentence and prints the number of words in it.

x=input("enter string:")
words = x.split()

print(f"count:{len(words)}")