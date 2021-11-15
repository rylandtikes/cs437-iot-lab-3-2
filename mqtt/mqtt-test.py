import paho.mqtt.client as mqtt
import time

broker_address="10.0.1.46"
shopper_telemetry = '''
[
  {
    "date": "2021-11-14",
    "id": 1,
    "face_inference_time": 29.916,
    "head_pose_inference_time": 9.195
  }
]
'''

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

while True:
    print("creating new instance")
    client = mqtt.Client("Test1")
    client.on_message=on_message
    print("connecting to broker")
    client.connect(broker_address)
    client.loop_start()
    print("Subscribing to topic","test/topic")
    client.subscribe("test/topic")
    print("Publishing message to topic","test/topic")
    client.publish("test/topic", shopper_telemetry)
    time.sleep(4)
    client.loop_stop()
