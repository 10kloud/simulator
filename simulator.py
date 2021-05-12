import time, json, random, math
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT
#read configuration
with open("json/configuration.json") as json_file:
    configuration = json.load(json_file)
#configuration IoT Core SDK
myAWSIoTMQTTClient = AWSIoTMQTT.AWSIoTMQTTClient("test")
myAWSIoTMQTTClient.configureEndpoint(configuration['endpoint'], configuration['port'])
myAWSIoTMQTTClient.configureCredentials(configuration['pem'],configuration['key'], configuration['crt'])

#other
topic = "Gruppo5/silios"
x = 0.00
limit  = 4
#functions
def Initiation():
    myAWSIoTMQTTClient.connect()
    print("Begin Publish...")
def Publish(data):
    global topic
    myAWSIoTMQTTClient.publish(topic, str(data), 1)
    print("To Topic: Gruppo5/Silios, Send it" )
def Close():
    myAWSIoTMQTTClient.disconnect()
def SilioSystem(i, siliosSystem, x):
    if(siliosSystem['silio'+str(i)]['startPosition'] == None):
        siliosSystem['silio'+str(i)]['startPosition'] = random.randint(0, 10) #random start level
        siliosSystem['silio'+str(i)]['slowness'] = random.uniform(0.1, 1.0) #random slowness
    siliosSystem['silio'+str(i)]['value'] = math.sin(x*siliosSystem['silio'+str(i)]['slowness']+siliosSystem['silio'+str(i)]['startPosition'])*limit+limit
    # sin(x*lunghezza+posizionePartenza)*3.5+3.5 <-- oscilla tra 0 e 7
    
#read silios data information
with open("json/siliosData.json") as json_file:
    siliosData = json.load(json_file)
print("load file: "+str(siliosData))
#read silios system
with open("json/siliosSystem.json") as json_file:
    siliosSystem = json.load(json_file)
print("load file: "+str(siliosSystem))
#main
time.sleep(5)
Initiation()
while True:
    for i in range(7):
        SilioSystem(i+1, siliosSystem, x)
        siliosData['silio'+str(i+1)]['sensors'] = int(siliosSystem['silio'+str(i+1)]['value'])
    print(json.dumps(siliosSystem, indent=4, sort_keys=True))
    print("X: "+str(x))
    Publish(siliosData)
    time.sleep(5)
    x += 0.1