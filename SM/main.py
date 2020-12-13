import paho.mqtt.client as mqtt

from SMClient import SMClient

smclient = SMClient("SM_CLIENT")
smclient.socket_listen()
