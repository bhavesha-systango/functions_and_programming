last_name = lambda name: name.split()[1]
print(last_name('Nikola Tesla'))

scientists = ['bhavesh', 'taher', 'praveen', 'rahul']
last = sorted(scientists, key=lambda name: name.split()[0])
print(last)

add = lambda a,b: a+b
print(add(5,7))

is_odd = lambda x: x % 2 == 1
print(is_odd(2))
