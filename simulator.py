import time, json, random, math
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT
#class
from IoTCore import IoTCore
from Silo import Silo
#read configuration
with open("json/configuration.json") as json_file:
    configuration = json.load(json_file)
#configuration IoT Core SDK
iotCore = IoTCore(configuration['pem'], configuration['key'], configuration['crt'], configuration['endpoint'], configuration['port'], configuration['topic'])
silo = Silo(7)
iotCore.StartConnection()
while True:
    data = silo.Event()
    #print(json.dumps(data, indent=4, sort_keys=True))
    for i in range(7):
        iotCore.Publish(data['silo'+str(i+1)])
    time.sleep(1)