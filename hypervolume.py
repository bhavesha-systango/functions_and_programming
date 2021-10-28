def hypervolume(*args):
    print(args)
    print(type(args))

hypervolume(3,4)
hypervolume(3,4,5)

def hypervolume2(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v*=length
    return v

print(hypervolume2(2,4))
print(hypervolume2(3,7,6,8))

def hypervolume3(length, *lengths):
    v = length
    for item in lengths:
        v *=item
    return v

print(hypervolume3(2,5))
