import paho.mqtt.client as mqtt

from MDMSClient import MDMSClient

smclient = MDMSClient("MDMS_CLIENT")
smclient.socket_listen()
