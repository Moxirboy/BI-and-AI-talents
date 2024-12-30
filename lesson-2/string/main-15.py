#Ask the user for a sentence and create an acronym from the first letters of each word.
x = input("Enter string: ")
acronym = x.split(" ")
result = ""
for x in acronym:
    result=result+x[0]
print(result)

