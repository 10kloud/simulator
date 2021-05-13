import json, random
from RandomSIN import RandomSIN
class Silio:
    def __init__(self, nSilios):
        #read silio data information
        with open("json/silioData.json") as json_file:
            self.silioData = json.load(json_file)
        print("load file: "+str(self.silioData))

        #read silio system
        with open("json/silioSystem.json") as json_file:
            self.silioSystem = json.load(json_file)
        print("load file: "+str(self.silioSystem))

        #set number silios
        self.nSilios = nSilios

        #set other parameter
        self.interval = 4
        self.time = 0.00
    def Event(self):
        for i in range(self.nSilios):
            k = i+1
            if(self.silioSystem['silio'+str(k)]['startPosition'] == None):
                self.silioSystem['silio'+str(k)]['startPosition'] = random.randint(0, 10) #random start level
                self.silioSystem['silio'+str(k)]['lenght'] = random.uniform(0.1, 1.0) #random lenght
            self.silioSystem['silio'+str(k)]['value'] = RandomSIN.Random(self.silioSystem['silio'+str(k)]['lenght'], self.silioSystem['silio'+str(k)]['startPosition'], self.interval, self.time)
            self.silioData['silio'+str(k)]['sensors'] = int(self.silioSystem['silio'+str(k)]['value'])
            return self.silioData
    