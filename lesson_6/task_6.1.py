class TrafficLight:
    def running(self):
        import time
        from itertools import cycle
        collist = ['красный', 'желтый', 'зеленый']
        for color in cycle(collist):
            if color == 'красный':
                time.sleep(7)
            elif color == 'желтый':
                time.sleep(2)
            elif color == 'зеленый':
                time.sleep(10)
            print(color)


a = TrafficLight()
a.running()
