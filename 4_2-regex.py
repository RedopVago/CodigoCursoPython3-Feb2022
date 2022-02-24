
import re

s1 = 'Hola, buenos dias a todos'
s2 = 'Hola, buenas tardes a todos'
s3 = 'Hola, buenas noches a todos'

p1 = 'dias'
p2 = 'noches'

p3 = 'buen[ao]s (.*) a'

ret = re.search(p3, s3)

if ret:

    print(f'grupos: {ret.groups()}')

    momento = ret.group(1)
    print(f'momento: {momento}')
else:
    print(f'No encontro coincidencias de "{p3}"')
