import math
class RandomSIN:
    def Random(lenght, startPosition, interval, interval1, time):
        return math.sin(time*lenght+startPosition)*interval+interval1
