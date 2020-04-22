from functools import reduce


def func_fact(x, y):
    return x * y


list1 = [int(i) for i in range(100, 1001) if i % 2 == 0]
print(list1)
print(reduce(func_fact, list1))
