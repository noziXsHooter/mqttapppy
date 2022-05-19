import os
import paho.mqtt.client as paho
from mqtt_client.mqtt_client import publish
from paho.mqtt import client as mqtt_client
import random
import time
from kivy.clock import Clock
from kivymd.app import MDApp
from kaki.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

#Atribuição do BROKER
broker = 'broker.hivemq.com'
port = 1883
topic = "nozix\ligarpeixes"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-nozix-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


from kivymd.uix.floatlayout import MDFloatLayout
from kivy.factory import Factory
Window.size = (350, 580)


class LiveApp(MDApp, App):


    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("init.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        #screen_manager.add_widget(Builder.load_file("home.kv"))
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.login, 1)

    def login(self, *args):
        screen_manager.current = "login"

    def verify(self, email, password):
        if email == "1" and password == "1":
            print('Your are logged in to IOT-PROJECT')
            self.root.current = 'home'

        else:
            print('Login or password incorrect')

class Home(GridLayout):
    pass


#    def on_switch_active(self, widget):
#        print("Switch: "+ str(widget.active))


'''#CONEXÃO DO MQTT
def connect_mqtt(self):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_publish(client,userdata,result):             #create function for callback
    print("Alimentador de peixes foi acionado! \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("nozix\ligarpeixes","ON")                   #publish

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    on_publish()
'''

# finally, run the app
if __name__ == "__main__":
    LiveApp().run()