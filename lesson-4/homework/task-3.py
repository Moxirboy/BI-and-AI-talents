txt = "abcabcabc"
vowels = ["a",'e','i','u','o']
i = 3
while(i<len(txt)):
    if i+1 == len(txt)-1:
        break
    if txt[i] in vowels:
        i = i + 1
    txt = txt[:i]+"_"+txt[i:]
    i = i + 3
print(txt)
