def check(func):
    def wrapper(*argc,**kwargc):
        try:
            c = func(*argc,**kwargc)
        except ZeroDivisionError:
            print("dominator cannot be zero")
        else:
            print(c)
    return wrapper

@check
def divisor(a,b):
    return a/b

divisor(4,0)
