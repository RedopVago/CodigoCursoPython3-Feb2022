import random

# crear un set
s1 = set()

print(f'tipo: {type(s1)}')


s1.add('uno')
s1.add('dos')
s1.add('tres')
s1.add('cuatro')
s1.add(5)
s1.add(6)

print(f'tamaño de s1: {len(s1)}')
print(s1)

item = s1.pop()

print(s1)
print(item)


s1.remove('uno')

print(s1)
print()
print()
print()

s2 = set()

for nr in range(10):
    n = random.randint(0, 100)
    print(n)
    s2.add(n)

print(s2)