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
        #level
        self.intervalLevel = 4.15
        #tempExternal
        self.intervalExternal = 20
        self.intervalExternal1 = 15
        #humidityExternal1
        self.humidityExternal = 0.5
        #humidityExternal1
        self.pressureInternal = 0.5
        self.time = 0.00
    def Event(self):
        for i in range(self.nSilios):
            k = i+1
            if(self.silioSystem['silio'+str(k)]['level']['startPosition'] == None):
                #random for level of the liquid
                self.silioSystem['silio'+str(k)]['level']['startPosition'] = random.randint(0, 10) #random start level
                self.silioSystem['silio'+str(k)]['level']['lenght'] = random.uniform(0.1, 1.0) #random lenght
                #random for the temperature min:-20 max:40
                self.silioSystem['silio'+str(k)]['tempExternal']['startPosition'] = 0.4 #start level
                self.silioSystem['silio'+str(k)]['tempExternal']['lenght'] = random.uniform(0.03, 0.05) #random lenght
                #random for umidity
                self.silioSystem['silio'+str(k)]['humidityExternal']['startPosition'] = -0.5 #start level
                self.silioSystem['silio'+str(k)]['humidityExternal']['lenght'] = random.uniform(0.08, 0.1) #random lenght
                #random for pressureInternal
                self.silioSystem['silio'+str(k)]['pressureInternal']['startPosition'] = 0.4 #start level
                self.silioSystem['silio'+str(k)]['pressureInternal']['lenght'] = self.silioSystem['silio'+str(k)]['tempExternal']['lenght'] #random lenght
            #random for level
            self.silioSystem['silio'+str(k)]['level']['value'] = RandomSIN.Random(self.silioSystem['silio'+str(k)]['level']['lenght'], self.silioSystem['silio'+str(k)]['level']['startPosition'], self.intervalLevel, self.intervalLevel, self.time)
            #random for tempExternal
            self.silioSystem['silio'+str(k)]['tempExternal']['value'] = RandomSIN.Random(self.silioSystem['silio'+str(k)]['tempExternal']['lenght'], self.silioSystem['silio'+str(k)]['tempExternal']['startPosition'], self.intervalExternal, self.intervalExternal1, self.time)
            #random for humidityExternal
            self.silioSystem['silio'+str(k)]['humidityExternal']['value'] = RandomSIN.Random(self.silioSystem['silio'+str(k)]['humidityExternal']['lenght'], self.silioSystem['silio'+str(k)]['humidityExternal']['startPosition'], self.humidityExternal, self.humidityExternal, self.time)
            #random for pressureInternal
            self.silioSystem['silio'+str(k)]['pressureInternal']['value'] = RandomSIN.Random(self.silioSystem['silio'+str(k)]['pressureInternal']['lenght'], self.silioSystem['silio'+str(k)]['pressureInternal']['startPosition'], self.humidityExternal, self.humidityExternal, self.time)
            #set level
            self.silioData['silio'+str(k)]['level'] = int(self.silioSystem['silio'+str(k)]['level']['value'])
            #set tempExternal
            self.silioData['silio'+str(k)]['tempExternal'] = int(self.silioSystem['silio'+str(k)]['tempExternal']['value'])
            #set humidityExternal
            self.silioData['silio'+str(k)]['humidityExternal'] = self.silioSystem['silio'+str(k)]['humidityExternal']['value']
            #set pressureInternal
            self.silioData['silio'+str(k)]['pressureInternal'] = self.silioSystem['silio'+str(k)]['pressureInternal']['value']
        print(json.dumps(self.silioSystem, indent=4, sort_keys=True))
        self.time += 0.1
        return self.silioData
    