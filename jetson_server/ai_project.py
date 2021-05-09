from jetcam.usb_camera import USBCamera
import torch
import torchvision
from utils import preprocess
import torch.nn.functional as F
import torchvision.transforms as transforms
from dataset import ImageClassificationDataset
import paho.mqtt.client as mqtt
import time

MQTT_HOST = 'xxx.xxx.xxx.xxx'
MQTT_PASSWORD = 'mqtt_password'
MQTT_USER = 'mqtt_user'
MQTT_CLIENT = 'game' 
MQTT_TOPIC = '/game'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        #client.subscribe("/game")
        print("Connected with code %d" % rc)

mqtt_client = mqtt.Client(MQTT_CLIENT)
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.connect(MQTT_HOST,port=1883, keepalive=600)
mqtt_client.loop_start()

camera = USBCamera(width=224, height=224, capture_device=0)
camera.running = True
print("Camera created")

DATASETS = ['A', 'B']
CATEGORIES = ['move_left', 'move_right', 'stop', 'launch_missile']
TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

datasets = {}
datasets['A'] = ImageClassificationDataset(
	'/nvdli-nano/data/classification/game_A', CATEGORIES, TRANSFORMS
	)
dataset = datasets['A']

device = torch.device('cuda')



model = torchvision.models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(512, len(dataset.categories))
model.to(device)
model.load_state_dict(torch.load('/nvdli-nano/data/classification/game_model_2.pth'))
model = model.eval()
previous_state = ""
start_time = time.time()
current_time = time.time()
delta_time = 0.3
while True:
    image = camera.value
    preprocessed = preprocess(image)
    output = model(preprocessed)
    output = F.softmax(output, dim=1).detach().cpu().numpy().flatten()
    category_index = output.argmax()
    #print(CATEGORIES[category_index], output)
    #print(CATEGORIES[category_index], output) 
    current_time = time.time() 
    if current_time - start_time > delta_time:
       previous_state ="" 
    if previous_state != CATEGORIES[category_index]:
        previous_state = CATEGORIES[category_index]
        start_time = time.time()
        mqtt_client.publish(MQTT_TOPIC, CATEGORIES[category_index], qos=0)

    
