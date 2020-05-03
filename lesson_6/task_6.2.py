class Road:
    _length = 50
    _width = 5
    def count(self, var1, var2):
        return var1 * var2 * Road._width * Road._length
r1 = Road()
print('масса асфальта', r1.count(25, 5), 'тонн')
