from kivy.app import App
import os
import json
import requests
import paho.mqtt.client as paho
from mqtt_client.mqtt_client import publish
from paho.mqtt import client as mqtt_client
import time
import random
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout

Window.size = (350, 492)

# Atribuição do BROKER
broker = 'broker.hivemq.com'
port = 1883
topic = "nozix/ligarpeixes"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-nozix-{random.randint(0, 1000)}'


# username = 'emqx'
# password = 'public'

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


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):

    def switchpeixes(self, instance, value, userdata=None, result=None):

        if value:
            print("Alimentador dos peixes está ON")

            # def on_publish(client, userdata, result):  # create function for callback
            # print("Alimentador de peixes foi acionado! \n")
            # pass

            client = paho.Client("control1")  # create client object
            # client.on_publish = on_publish  # assign function to callback
            client.connect(broker, port)  # establish connection
            ret = client.publish("bombasub777test", "LIGADO")  # publish
            client = connect_mqtt(self)
            # client.loop_start()
            # publish(client)
            # on_publish(client, userdata, result)
            # client.loop_stop()
            # client.disconnect()

            # TESTAR O CALLBACK!!!!!!

        else:
            print("Alimentador dos peixes está OFF")

            def on_publish(client, userdata, result):  # create function for callback
                print("Alimentador de peixes foi desligado! \n")
                pass

            client = paho.Client("control1")  # create client object
            client.on_publish = on_publish  # assign function to callback
            client.connect(broker, port)  # establish connection
            ret = client.publish("bombasub777test", "DESLIGADO")  # publish
            client = connect_mqtt(self)
            # client.loop_start()
            # publish(client)
            # on_publish(client, userdata, result)
            # client.loop_stop()
            # client.disconnect()

    def switchbomba(self, instance, value):

        if value:
            print("A bomba está ON")
        else:
            print("A bomba está OFF")

    def switchluz1(self, instance, value):

        if value:
            print("A luz1 está ON")
        else:
            print("A luz1 está OFF")

    def switchluz2(self, instance, value):

        if value:
            print("A luz2 está ON")
        else:
            print("A luz2 está OFF")

    def switchluz3(self, instance, value):

        if value:
            print("A luz3 está ON")
        else:
            print("A luz3 está OFF")

    def switchluz4(self, instance, value):

        if value:
            print("A luz4 está ON")
        else:
            print("A luz4 está OFF")


class WindowManager(ScreenManager):

    def on_connect(client, userdata, flags, rc):
        print("Conectado no mqtt como subscriber")
        client.subscribe("bombapub777")

    def on_message(client, userdata, msg):
        peixesd = "DESLIGADO"
        peixesl = "LIGADO"
        global peixes
        print("TOPIC - " + msg.topic + " " + "----  PAYLOAD - " + str(msg.payload))
        peixes = str(msg.payload)

        if (peixes == "b'DESLIGADO'"):
            print('TUDO DESLIGADO')
        elif (peixes == "b'LIGADO'"):
            print('TUDO LIGADO')
        else:
            print('ESTADO INVALIDO!')

        # EXEMPLO LOGICA PARA FORMATAÇÃO DO PAYLOAD
        '''
        lenght = len(peixes)
        #print(type(lenght))
        if (lenght == 9):
            peixes = peixes[2:8]
            print(peixes)

        elif (lenght == 12):
            peixes = peixes[2:11]
            print(peixes)
        else:
            print('Lenght Incorreto!')

        if (peixes == peixesd):
            print('TUDO DESLIGADO')
        elif (peixes == peixesl):
            print('TUDO LIGADO')
        else:
            print('ESTADO INVALIDO!')
        '''

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    client.loop_start()


kv = Builder.load_file('home.kv')


class Appp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return kv


# def run():
# client = connect_mqtt()
# client.loop_start()
# publish(client)
# on_publish()

if __name__ == "__main__":
    Appp().run()
