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
