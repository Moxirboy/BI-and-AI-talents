#Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).
x=int(input("enter number for list of words:"))
words=[]
for _ in range(x):
    word=input("enter word: ")
    words.append(word)
    
sentences='-'.join(words)
print(f"you entered words: {sentences}")