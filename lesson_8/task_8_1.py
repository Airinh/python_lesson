from datetime import datetime, date


class Data:

    def __init__(self, data: str):
        self.data = data


    @classmethod
    def conv(cls, data):
        temp = data.split('-')
        x = int(temp[2])
        y = int(temp[1])
        z = int(temp[0])
        dt = datetime(x, y, z)
        return dt.date()

    @staticmethod
    def valid(data):
        temp = data.split('-')
        try:
            if int(temp[0]) > 31 or int(temp[1]) > 12 or int(temp[2]) > 2020:
                print('дата введена неверно')
        except ValueError:
            print('дата введена неверно')


d1 = '40-12-2020'
Data.valid(d1)
d2 = '12-12-2002'
print (type((Data(d2))))
print(type((Data.conv(d2))))
