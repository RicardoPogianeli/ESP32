import paho.mqtt.client as mqtt
import time

user = 'f5657b50-21e8-11eb-a2e4-b32ea624e442'
password = 'f1dcea17936e64dc8a45c464dd5f078b8605a83e'
client_id = 'c4e80d80-21ed-11eb-a2e4-b32ea624e442'
server = 'mqtt.mydevices.com'
port = 1883

publish_0 = 'v1/'+user+'/things/'+client_id+'/data/0'
publish_1 = 'v1/'+user+'/things/'+client_id+'/data/1'
subscribe_2 = 'v1/'+user+'/things/'+client_id+'/cmd/2'

def mensagens(client, userdate, msg):
    m = msg.topic.split('/')
    p = msg.payload.decode().split(',')
    print(m)
    print(p)
    print("ok")

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server,port)
client.on_message = mensagens
client.subscribe(subscribe_2)

client.loop_start()

for i in range(1, 10):
    client.publish(publish_0, i)
    client.publish(publish_1, i*2.1)
    time.sleep(2)