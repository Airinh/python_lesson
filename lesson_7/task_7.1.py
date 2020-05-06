class Matrix:
    def __init__(self, *args):
        self.mlist = []
        self.mlist_sum = []
        for el in args:
            self.mlist.append(el)

    def __str__(self):
        self.mlist_str = ''
        for el in self.mlist:
             self.mlist_str = f'{self.mlist_str} {el} \n'
        return self.mlist_str

    def __add__(self, other):
        test = 1
        if len(self.mlist) != len(other.mlist):
            print('сложение матриц разного размера невозможно')
        else:
            for y in range(0, len(self.mlist)):
                str1 = self.mlist[y]
                str2 = other.mlist[y]
                str3 = []
                if len(str1) != len(str2):
                    print('сложение матриц разного размера невозможно')
                    test = 0
                    break
                else:
                    for x in range(0, len(str1)):
                        str3.append(str1[x] + str2[x])
                    self.mlist_sum.append(str3)
            if test == 1:
                return Matrix(*self.mlist_sum)


m1 = Matrix([1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 6])
m2 = Matrix([1, 0, 0, 1], [0, 1, 0, 0],  [0, 0, 1, 0])
print(m1)
m3 = m1 + m2
print(m3)
