def sequence_class(immutable):
    return tuple if immutable else list

seq = sequence_class(immutable = False)
s = seq("Nairobi")
s
print(s)
print(type(s))