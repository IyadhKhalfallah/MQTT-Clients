import paho.mqtt.client as mqtt
import threading
from datetime import datetime

class SMClient:
    def __init__(self, id):
        self.id= id
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def socket_listen(self):
        self.client.connect("0.0.0.0", 1883, 60)
        self.consommation_pub()
        self.production_pub()
        self.client.loop_forever()

    # High Quality Of Service
    def consommation_pub(self,consommation=10):
        self.client.publish("consommation", qos=2, payload= "client with id " + str(self.id) +" sent consumption " + str(consommation))
        threading.Timer(60.0*60.0, self.consommation_pub).start()

    # High Quality Of Service
    def production_pub(self, production=10):
        self.client.publish("production", qos=2, payload="client with id " + str(self.id) +" sent production " + str(production))
        threading.Timer(60.0*15.0, self.production_pub).start()





    # Callbacks 
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("reduction")
        client.subscribe("prix")
    @staticmethod
    def on_message(client, userdata, msg):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time+" "+msg.topic+" "+str(msg.payload))