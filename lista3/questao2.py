
def decorator_1(func):
    def inner(*args, **kwargs):
        
        print("Início decorator")
        value = func(*args, **kwargs)
        print("final decorator")
        
        return value
    return inner

@decorator_1
def which_is_max(a,b):
    if a > b:
        print("a é maior com valor " + str(a))
        return
    print("a é maior com valor " + str(b))

which_is_max(2,5)

