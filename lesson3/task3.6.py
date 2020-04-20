def int_func(word):
    word = word.title()
    return word
test = 'да'
var = '0'
while test == 'да':
    list2 = []
    list1 = input('введите слова через пробел: ').split(' ')
    for int in list1:
        var = str(int)
        list2.append(int_func(var))
    print(list2)
    test = input('хотите проолжить? (да/нет)')
    test = test.lower()
