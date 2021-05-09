import os
import pygame
from Player import Player
from Missile import Missile
from Enemy import Enemy
import paho.mqtt.client as mqtt

MQTT_HOST = 'xxx.xxx.xxx.xxx'
MQTT_PASSWORD = 'mqtt_password'
MQTT_USER = 'mqtt_user'
MQTT_CLIENT = 'game_client'
MQTT_TOPIC = '/game'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        client.subscribe("/game")
        print("Connected with code %d" % rc)


def on_message( client, userdata, message):
    # time.sleep(1)
    print("Topic: " + str(message.topic))
    print("Message: " + str(message.payload))
    print("received message =", str(message.payload.decode("utf-8")))
    print(str(message.topic))
    if str(message.topic) == "/game":
        if str(message.payload.decode("utf-8")) == 'move_left':
            mqtt_event = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741904, 'mod': 4096, 'scancode': 80, 'window': None})
            pygame.event.post(mqtt_event)
        if str(message.payload.decode("utf-8")) == 'move_right':
            mqtt_event = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})
            pygame.event.post(mqtt_event)
        if str(message.payload.decode("utf-8")) == 'stop':
            mqtt_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
            pygame.event.post(mqtt_event)
        if str(message.payload.decode("utf-8")) == 'launch_missile':
            mqtt_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
            pygame.event.post(mqtt_event)


mqtt_client = mqtt.Client(MQTT_CLIENT)
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_HOST, port=1883, keepalive=600)
mqtt_client.loop_start()

WIDTH = 640
HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI project")
clock = pygame.time.Clock()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
bg_img = pygame.image.load(os.path.join(img_folder, 'bg.png')).convert()

game_run = True
all_sprites = pygame.sprite.Group()
player = Player()
# missile = Missile()
all_sprites.add(player)

MISSILES = []
ENEMIES = []
for x in range(10, WIDTH - 60, 60):
    ENEMIES.append(Enemy(x, 100))
ENEMY_HIT = 0


def display_score(display_screen):
    global ENEMIES
    global game_run
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Points : {}".format(ENEMY_HIT), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (90, 30)
    display_screen.blit(text, textRect)
    enemies_text = font.render("Enemies left : {}".format(len(ENEMIES)), True, WHITE)
    textRect = enemies_text.get_rect()
    textRect.center = (480, 30)
    display_screen.blit(enemies_text, textRect)
    if len(ENEMIES) == 0:
        game_run = False


def check_collisions(missiles, enemies):
    global ENEMY_HIT
    for missile in missiles:
        missile_pos = missile.get_position()
        for enemy in enemies:
            enemy_pos = enemy.get_position()
            if (missile_pos[0] >= enemy_pos[0] and missile_pos[0] + 21 <= enemy_pos[0] + 50) and \
                    (missile_pos[1] >= enemy_pos[1] and missile_pos[1] + 25 <= enemy_pos[1] + 30):
                enemy.is_hit = True
                missile.explode()
                ENEMY_HIT += 1


while game_run:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))
    display_score(screen)
    for enemy in ENEMIES:
        if enemy.is_on_screen():
            screen.blit(enemy.image, enemy.rect)
            enemy.update()
        if not enemy.is_on_screen():
            ENEMIES.remove(enemy)
    for mis in MISSILES:
        if mis.is_on_screen():
            screen.blit(mis.image, mis.rect)
            mis.update()
        else:
            MISSILES.remove(mis)

    check_collisions(MISSILES, ENEMIES)
    all_sprites.update()
    for event in pygame.event.get():
        # print(event)
        keys = pygame.key.get_pressed()
        # pygame.key.get_repeat()

        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_LEFT] or event.key == pygame.K_LEFT:
                player.move_left()
            if keys[pygame.K_RIGHT] or event.key == pygame.K_RIGHT:
                player.move_right()
            if keys[pygame.K_SPACE] or event.key == pygame.K_SPACE:
                position = player.get_position()
                MISSILES.append(Missile(position[0], position[1]))
    # screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
