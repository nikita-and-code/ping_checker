from ping3 import ping
from pystray import MenuItem as item
from pystray import Icon as icon
from PIL import Image, ImageDraw
import time
import threading
import pystray

# Глобальное состояние иконки
color = 'green'

# Функция для создания иконки определенного цвета
def create_image(i):
    image = Image.new('RGB', (64, 64), i)
    return image

# Функция для обработки пинга
def pinger():
    global color
    while True:
        if type(ping('example.com')) == float:
            color = 'green'
            print(color)
            time.sleep(1)
        else:
            color = 'red'
            print(color)
            time.sleep(1)


thread1 = threading.Thread(target=pinger)
thread1.start()

def icon_updater(i):
    while True:
        icon = pystray.Icon(
            'test name',
            icon=create_image(i))

thread2 = threading.Thread(target=icon_updater, args=(color,))
thread2.start()

icon.run()

