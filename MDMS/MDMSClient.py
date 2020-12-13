import paho.mqtt.client as mqtt
import threading
from datetime import datetime

class MDMSClient:

    def __init__(self, id):
        self.id= id
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def socket_listen(self):
        self.client.connect("0.0.0.0", 1883, 60)
        self.prix_pub()
        self.reduction_pub()
        self.client.loop_forever()

    # Lower Quality Of Service
    def prix_pub(self,prix=10):
        self.client.publish("prix", qos=1, payload= "client with id " + str(self.id) +" sent price " + str(prix))
        threading.Timer(60.0*60.0, self.prix_pub).start()

    # High Quality Of Service
    def reduction_pub(self, reduction=3):
        self.client.publish("reduction", qos=2, payload= "client with id " + str(self.id) +" sent reduction " + str(reduction))
        threading.Timer(60.0, self.reduction_pub).start()




    # Callbacks 
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("production")
        client.subscribe("consommation")
         
    @staticmethod
    def on_message(client, userdata, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time+" "+msg.topic+" "+str(msg.payload))