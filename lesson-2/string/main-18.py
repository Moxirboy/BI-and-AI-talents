sen = input("input: ")
start = input("start: ")
end = input("end: ")


if sen.startswith(start) and sen[::-1].startswith(end[::-1]):
    print("match")
else:
    print("doesn`t match")
