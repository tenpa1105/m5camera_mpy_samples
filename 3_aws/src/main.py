import gc
import camera
import utime
import config
import ujson
import ubinascii
from umqtt.robust import MQTTClient

CLIENT_ID = "m5camera"
TOPIC = "data/camera/" + CLIENT_ID

with open(config.CLI_CERT_PATH, 'r') as f:
  CLI_CERT = f.read()
with open(config.CLI_PRIV_KEY_PATH, 'r') as f:
  CLI_PRIV_KEY = f.read()

client = MQTTClient(client_id=CLIENT_ID,
                   server=config.AWS_IOT_ENDPOINT,
                   port = 8883,
                   keepalive = 10000,
                   ssl = True,
                   ssl_params = {
                     "cert": CLI_CERT,
                     "key": CLI_PRIV_KEY,
                     "server_side":False
                   } )
try:
    client.connect()
    while True:
        img = camera.capture()
        payload= {"image": ubinascii.b2a_base64(img.to_bytes())}
        print("publish:", TOPIC )
        client.publish(TOPIC, ujson.dumps(payload))

        utime.sleep(5)
except Exception as e:
    print(e)


