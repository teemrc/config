from map import Map
from helec import Helicopter as Helico
import time, os, json
from pynput import keyboard
from clouds import Clauds

# 🌲 🌊 🚁🟩 🔥 🏥 💛 💵 ⬛ 🚰 🏆 ☁️ 🌩️ 🔲 🧳 ⛅ 

TICK_SLEEP = 0.2
TREE_UPD = 50
FIRE_UPD = 60
CLOUDS_UPD = 30
MAP_W, MAP_H = 20, 10


field = Map(MAP_W, MAP_H)
field.generate_f(3, 10)
field.generate_r(10)
field.generate_r(10)
field.generate_r(10)

clouds = Clauds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def proccess_key(key):
    global helico, tick, clouds, field
    
    c = key.char.lower()
    # Обработка движений вертолета
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    
    if c == 'f':
        data = {'helicopter': helico.exdata(),
                'clouds': clouds.exdata(),
                'field': field.exdata(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
        
    if c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.importData(data['helicopter'])
            field.imdata(data['field'])
            clouds.imdata(data['clouds'])

listener = keyboard.Listener(
    on_press = None,
    on_release = proccess_key)
listener.start()

while True:
    os.system('cls')
    field.prochelico(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print('Tick', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPD == 0):
        field.generate_tree()
    if (tick % FIRE_UPD == 0):
        field.upd_fire()
    if (tick % CLOUDS_UPD == 0):
        clouds.upd_clouds()
