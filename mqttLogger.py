import paho.mqtt.client as mqtt
import logging

# Setup the log file
logging.basicConfig(filename='mqtt.log',level=logging.INFO, format='%(asctime)s %(message)s')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("say");
    client.subscribe("english");
    client.subscribe("french");
    client.subscribe("japanese");
    client.subscribe("test");
    client.subscribe("can");  #CAN data in JSON

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    logging.info(msg.topic+" "+str(msg.payload))  # log the messages from the MQTT broker

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("hri.stanford.edu", 8134, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
