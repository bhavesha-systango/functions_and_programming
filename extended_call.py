def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11,12,13,14)
print_args((*t))

def color(red, green, blue, **kwargs):
    print(red)
    print(green)
    print(blue)
    print(kwargs)

k = {'red':21, 'green':36, 'blue':48, 'alpha':72}
color(**k)

def trace(*args, **kwargs):
    print("args=",args)
    print("kwargs=",kwargs)

trace(11,12,base=16, base2=32)

def trace2(f, *args, **kwargs):
    print("args=",args)
    print("kwargs=",kwargs)
    result = f(*args,**kwargs)
    print("result=", result)

trace2(int, "ff", base=16)


