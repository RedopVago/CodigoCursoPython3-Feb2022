
import time
from threading import Thread

def sleeper(i):
    print(f'Thread-{i} espera {10-i} segundos')
    time.sleep(10 - 2*i) 
    print(f'Thread-{i} termina')

for i in range(5):
    print(f'Creando Thread-{i}')
    t = Thread(target=sleeper, args=(i,))
    t.start()

print('FIN')