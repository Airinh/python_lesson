from itertools import cycle
from time import sleep
for el in cycle([1, 2, 3, 4, 5]):
    print(el)
    sleep(0.5)
