from time import sleep
from itertools import cycle


class TrafficLight():
    def __init__(self):
        self.colors = ['red', 'yellow', 'green', 'yellow']
        self.color_duration = {'red': 7, 'yellow': 2, 'green': 8}
        self.__color = 'red'

    def state(self, __color):
        print(__color)
        sleep(self.color_duration[__color])

    def running(self, iter=2):
        color_cycle = cycle(self.colors)
        for __color in color_cycle:
            try:
                self.state(__color)
            except KeyboardInterrupt:
                print('Светофор остановлен')
                exit()


TF = TrafficLight()
TF.running()
