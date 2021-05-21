import json, random
from RandomSIN import RandomSIN
class Silo:
    def __init__(self, nSilos):
        #read silo data information
        with open("json/siloData.json") as json_file:
            self.siloData = json.load(json_file)
        print("load file: "+str(self.siloData))

        #read silo system
        with open("json/siloSystem.json") as json_file:
            self.siloSystem = json.load(json_file)
        print("load file: "+str(self.siloSystem))

        #set number silos
        self.nSilos = nSilos

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
        for i in range(self.nSilos):
            k = i+1
            if(self.siloSystem['silo'+str(k)]['level']['startPosition'] == None):
                #random for level of the liquid
                self.siloSystem['silo'+str(k)]['level']['startPosition'] = random.randint(0, 10) #random start level
                self.siloSystem['silo'+str(k)]['level']['lenght'] = random.uniform(0.1, 1.0) #random lenght
                #random for the temperature min:-20 max:40
                self.siloSystem['silo'+str(k)]['tempExternal']['startPosition'] = random.uniform(-0.1,0.1) #start level
                self.siloSystem['silo'+str(k)]['tempExternal']['lenght'] = random.uniform(0.03, 0.05) #random lenght
                #random for umidity
                self.siloSystem['silo'+str(k)]['humidityExternal']['startPosition'] = -0.5 #start level
                self.siloSystem['silo'+str(k)]['humidityExternal']['lenght'] = random.uniform(0.08, 0.1) #random lenght
                #random for pressureInternal
                self.siloSystem['silo'+str(k)]['pressureInternal']['startPosition'] = self.siloSystem['silo'+str(k)]['tempExternal']['startPosition'] #start level
                self.siloSystem['silo'+str(k)]['pressureInternal']['lenght'] = self.siloSystem['silo'+str(k)]['tempExternal']['lenght'] #random lenght
            #random for level
            self.siloSystem['silo'+str(k)]['level']['value'] = RandomSIN.Random(self.siloSystem['silo'+str(k)]['level']['lenght'], self.siloSystem['silo'+str(k)]['level']['startPosition'], self.intervalLevel, self.intervalLevel, self.time)
            #random for tempExternal
            self.siloSystem['silo'+str(k)]['tempExternal']['value'] = RandomSIN.Random(self.siloSystem['silo'+str(k)]['tempExternal']['lenght'], self.siloSystem['silo'+str(k)]['tempExternal']['startPosition'], self.intervalExternal, self.intervalExternal1, self.time)
            #random for humidityExternal
            self.siloSystem['silo'+str(k)]['humidityExternal']['value'] = RandomSIN.Random(self.siloSystem['silo'+str(k)]['humidityExternal']['lenght'], self.siloSystem['silo'+str(k)]['humidityExternal']['startPosition'], self.humidityExternal, self.humidityExternal, self.time)
            #random for pressureInternal
            self.siloSystem['silo'+str(k)]['pressureInternal']['value'] = RandomSIN.Random(self.siloSystem['silo'+str(k)]['pressureInternal']['lenght'], self.siloSystem['silo'+str(k)]['pressureInternal']['startPosition'], self.humidityExternal, self.humidityExternal, self.time)
            #set level
            self.siloData['silo'+str(k)]['level'] = int(self.siloSystem['silo'+str(k)]['level']['value'])
            #set tempExternal
            self.siloData['silo'+str(k)]['tempExternal'] = int(self.siloSystem['silo'+str(k)]['tempExternal']['value'])
            #set humidityExternal
            self.siloData['silo'+str(k)]['humidityExternal'] = self.siloSystem['silo'+str(k)]['humidityExternal']['value']
            #set pressureInternal
            self.siloData['silo'+str(k)]['pressureInternal'] = self.siloSystem['silo'+str(k)]['pressureInternal']['value']
        print(json.dumps(self.siloSystem, indent=4, sort_keys=True))
        self.time += 0.1
        return self.siloData
    