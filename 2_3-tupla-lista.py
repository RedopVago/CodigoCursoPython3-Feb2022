
t1 = (1, 4.5, 'hole', [1,2,3])
l1 = [1*2, 4.5*2, 'hole', [4,5,6]]

try:
    l1[5] = 'hola'
except TypeError:
    print('No se permite modificar la tuplas')
except IndexError:
    print('El tamaño de la lista es menor')


l1[2] = 'hola'

t1 = tuple(l1)

l2 = list(t1)

# print(l2)

# print(t1)

# print(l1[3])


print(l2)
l2.append({'a','b','c'})
print(l2)

l2.insert(3, 'nuevo')
print(l2)

item = l2.pop()
print(item)
print(l2)


item2 = l2.pop(2)
print(item2)
print(l2)

l2.insert(3, 9.0)
print(l2)

l2.remove(9.0)
print(l2)


l2.remove(9.0)
print(l2)