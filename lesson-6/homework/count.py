import re
import string
import os

def count(name='employee.txt'):
    occurs = {}
    with open('name',mode='r') as f:
        line = f.readline()
        if not line:
            return occurs
        words = re.split(r' ',line)
        for word in words:
            new = re.sub(f"[{re.escape(string.punctuation)}]", "", word)
            if new not in occurs:
                occurs[new] = 1
            else:
                occurs[new] +=1
    return occurs
name = "sample.txt"
try:
    words = count(name)
except FileNotFoundError:
    print("file not found please enter file name to create")
    name = input()
    print("enter your text")
    with open(name+".txt",mode='w') as f:
        f.write(input())
    words = count(name)
print(words)
