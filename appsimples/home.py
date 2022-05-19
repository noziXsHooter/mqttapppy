from kivy.uix.screenmanager import ScreenManager, Screen
import paho.mqtt.client as paho
from mqtt_client.mqtt_client import publish
from paho.mqtt import client as mqtt_client
import random
from kivymd.uix.button import MDFloatingActionButton
from kivy.lang import Builder
from kivymd.app import MDApp

class home(Screen):
    pass

#Atribuição do BROKER
broker = 'broker.hivemq.com'
port = 1883
topic = "nozix\ligarpeixes"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-nozix-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def on_publish(client,userdata,result):             #create function for callback
    print("Alimentador de peixes foi acionado! \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("nozix\ligarpeixes","ON")                   #publish
