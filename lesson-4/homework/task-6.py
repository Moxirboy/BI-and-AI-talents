def isPrime(a):
    if a == 2:
        return True
    for i in range(2,int(a**0.5),1):
        if a%i==0:
            return False
    return True

for i in range(1,100,1):
    isprime = isPrime(i)
    if isprime:
        print(f"prime: {i}")
