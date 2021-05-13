import math
class RandomSIN:
    def Random(lenght, startPosition, interval, time):
        return math.sin(time*lenght+startPosition)*interval+interval
