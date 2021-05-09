# game client

Before run game client you need to  install `pygame` and `paho-mqtt` modules
```
pip3 install pygame
pip3 install paho-mqtt
```
Fill you own credential for mqtt server in `main.py`
```
MQTT_HOST = 'xxx.xxx.xxx.xxx'
MQTT_PASSWORD = 'mqtt_password'
MQTT_USER = 'mqtt_user'
```

You can install your own mqtt server like mosquitto
For detail information look at https://mosquitto.org/download/

And run `main.py` from console
```
cd game_client
python3 main.py
```

# How to play
After start main.py on laptop and start jetson server part you can play.
Show to jetson nano camera hand with this signs:
* move left
* move right
* stop
* launch missile
