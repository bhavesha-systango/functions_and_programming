result = map(ord,'the quick brown fix')
print(next(result))

class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

result = map(Trace()(ord), 'The quick brown fix')
print(next(result))
for i in map(ord,'the quick brown fix'):
    print(i)

print(list(map(ord,'the quick brown fix')))

sizes = ['small', 'medium', 'large']
colors = ['blue', 'green', 'red']
animals = ['peacock','rabbit','cockroach']

def combine(quantity, sizes, color, animals):
    return '{} * {} {} {}'.format(quantity, sizes, color, animals)

result2= combine(2,sizes, colors, animals)
print(result2)

import itertools
result3 = list(map(combine, itertools.count(),sizes,colors,animals))
print(result3)

