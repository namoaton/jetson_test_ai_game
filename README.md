# Jetson Nano server side
Copy `game_mode_2.pth` to `~/nvdli-data/classification` folder<br>
Copy `ai_project.py`, `dataset.py`, `utils.py` to `~/nvdli-data` folder<br>
<br>
 Run docker from course
 ```
 sudo docker run --runtime nvidia -it --rm --network host \
 --volume ~/nvdli-data:/nvdli-nano/data \
 --device /dev/video0 \
 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0 \
 ```
 
 Install paho-mqtt
 ```
 pip3 install paho-mqtt
 ```
 Fill host, user and password for mqtt server in `ai_project.py`
 ```
MQTT_HOST = 'xxx.xxx.xxx.xxx'
MQTT_PASSWORD = 'mqtt_password'
MQTT_USER = 'mqtt_user'
 ```
 Run application
 ```
 python3 ai_project.py
 ```


# game client
![game](https://github.com/namoaton/jetson_test_ai_game/raw/main/images/game.png)
<br>Before run game client you need to  install `pygame` and `paho-mqtt` modules
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
* move left <br>![move_left](https://github.com/namoaton/jetson_test_ai_game/raw/main/images/move_left.jpg)
* move right <br>![move_right](https://github.com/namoaton/jetson_test_ai_game/raw/main/images/move_right.jpg)
* stop<br>![stop](https://github.com/namoaton/jetson_test_ai_game/raw/main/images/stop.jpg)
* launch missile <br>![launch_missile](https://github.com/namoaton/jetson_test_ai_game/raw/main/images/launch_missile.jpg)

