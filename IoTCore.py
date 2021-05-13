import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT
class IoTCore:
    def __init__(self, pem, key, crt, endpoint, port, topic):
        self.myAWSIoTMQTTClient = AWSIoTMQTT.AWSIoTMQTTClient("Gruppo5-clod2021")
        self.myAWSIoTMQTTClient.configureEndpoint(endpoint, port)
        self.myAWSIoTMQTTClient.configureCredentials(pem, key, crt)
        self.topic = topic
        print("Configuration success!")
    def StartConnection(self):
        try:
            self.myAWSIoTMQTTClient.connect()
            print("Start MQTTClient")
        except:
            print("Error start MQTTClient")
    def CloseConnection(self):
        self.myAWSIoTMQTTClient.disconnect()
    def Publish(self, data):
        try:
            self.myAWSIoTMQTTClient.publish(self.topic, json.dumps(data), 0)
            print("Shipped success!")
            print("Data: "+str(data))
        except:
            print("Error send message to MQTT Broke")
