def convert_cel_to_fer(cel):
    return cel * (9/5) +32
def convert_fer_to_cel(fer):
    return (fer-32)*5/9

cer = int(input("enter celcuius: "))
fer = convert_cel_to_fer(cer)
print(f"cer to fer is {fer}")
fer = int(input("enter ferinheit: "))
cer = convert_fer_to_cel(fer)
print(f"fer to cer is {cer}")
