#Write a program that counts the number of vowels and consonants in a given string.
vowel='aeuio'
strr=input("Enter your string:")
vowels=0
consonants=0
for i in strr:
    if i in vowel:
        vowels=vowels+1
    else:
        consonants=consonants+1
print(f"vowels:{vowels}\nconsonants:{consonants}")