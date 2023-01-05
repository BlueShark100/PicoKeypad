import time
import picokeypad as keypad
import random
from machine import Pin

keypad.init()
keypad.set_brightness(1.0)

keypressed = keypad.get_button_states()

print("")
print("Entering: Memory")
memory = []
missed_key = 0
r = 255
g = 255
b = 255

SPPED = 0
Godlike = 0
Normal = 0

number_of_items = 0
show_button_speed = 1

rgb = []
rgb_numb = []

def clear_board():
    for i in range(0, 16):
        keypad.illuminate(i, 0, 0, 0)
    keypad.update()

out = 0
gottem = 1

last_button_states = 0
next_button = random.randint(0, 15)

for i in range(15, -1, -1):
    keypad.illuminate(i, 0, 0, 0)
    keypad.update()
    time.sleep(0.05)

while True:
    for i in range (0, 1):
        keypad.illuminate(5, 0, 0, 255)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(5, 0, 0, 0)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(5, 0, 0, 255)
    keypad.update()
    
    for i in range (0, 1):
        keypad.illuminate(6, 255, 255, 0)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(6, 0, 0, 0)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(6, 255, 255, 0)
    keypad.update()
    while True:
        keypressed = keypad.get_button_states()
        if SPPED == 1:
            break
        if Normal == 1:
            break
        if Godlike == 1:
            break
        if last_button_states != keypressed:
            last_button_states = keypressed
            if keypressed > 0:
                if keypressed == 32:
                    print("Normal Mode")
                elif keypressed == 64:
                    print("SPEED")
                    SPPED = 1
                elif keypressed == 256:
                    print("Godlike")
                    Godlike = 1
    while True:
        clear_board()
        next_button = random.randint(0, 15)
        memory.append(next_button)
        number_of_items = number_of_items + 1
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = [r, g, b]
        rgb_numb.append(rgb)
        
        time.sleep(0.5)
        if SPPED == 1:
            show_button_speed = 0.1
        if Normal == 1:
            if number_of_items == 6: #if they reach 5 make the show speed faster
                show_button_speed = 0.75
                print("sped up")
            elif number_of_items == 11:
                show_button_speed = 0.45
                print("sped up")
        if Godlike == 1:
            show_button_speed = 0
        
        print("")
        print("Showing Sequence")
        print("--Pay attention--")
        print("")
        for i in range(0, number_of_items): #show pattern
            rgb = rgb_numb[i]
            keypad.illuminate(memory[i], rgb[0], rgb[1], rgb[2])
            keypad.update()
            time.sleep(show_button_speed)
        time.sleep(0.35) #time between finish and show next pattern
        print(memory)
        clear_board()
        
        for i in range(0, number_of_items):
            out = 0
            if gottem == 0:
                break
            while True:
                if out == 1:
                    break
                keypressed = keypad.get_button_states()
                if last_button_states != keypressed:
                    last_button_states = keypressed
                    if out == 1:
                        break
                    if keypressed > 0:
                        if keypressed == 1: #0   #sets the correct column and row for the key pressed, I brute forced it
                            keypressed = 0
                        elif keypressed == 2: #1
                            keypressed = 1
                        elif keypressed == 4: #2
                            keypressed = 2
                        elif keypressed == 8: #3
                            keypressed = 3
                        elif keypressed == 16: #4
                            keypressed = 4
                        elif keypressed == 32: #5
                            keypressed = 5
                        elif keypressed == 64: #6
                            keypressed = 6
                        elif keypressed == 128: #7
                            keypressed = 7
                        elif keypressed == 256: #8
                            keypressed = 8
                        elif keypressed == 512: #9
                            keypressed = 9
                        elif keypressed == 1024: #A(10)
                            keypressed = 10
                        elif keypressed == 2048: #B(11)
                            keypressed = 11
                        elif keypressed == 4096: #C(12)
                            keypressed = 12
                        elif keypressed == 8192: #D(13)
                            keypressed = 13
                        elif keypressed == 16384: #E(14)
                            keypressed = 14
                        elif keypressed == 32768: #F(15)
                            keypressed = 15
                            
                        if keypressed == memory[i]:
                            print("nice")
                            rgb = rgb_numb[i]
                            keypad.illuminate(memory[i], rgb[0], rgb[1], rgb[2])
                            keypad.update()
                            gottem = 1
                            out = 1
                            time.sleep(0.05)
                        else:
                            gottem = 0
                            out = 1
                            missed_key = memory[i]
                            rgb = rgb_numb[i]
                        break
        if gottem == 0:
            break
        time.sleep(0.3)
    print("")
    print("-- Good Game --")
    print("Your Score:", number_of_items)
    print("Key Missed:", missed_key)
    print("")
    for i in range(0, 16):
        keypad.illuminate(i, 255, 0, 0)
        keypad.update()
        time.sleep(0)
    time.sleep(0.5)
    for i in range(0, 16):
        keypad.illuminate(i, 0, 0, 0)
        keypad.update()
        time.sleep(0.01)
    time.sleep(0.1)
    for i in range(0, 2): #show missed key
        keypad.illuminate(missed_key, rgb[0], rgb[1], rgb[2])
        keypad.update()
        time.sleep(0.15)
        keypad.illuminate(missed_key, 0, 0, 0)
        keypad.update()
        time.sleep(0.15)
    time.sleep(0.6)
    for i in range (0, 1):
        keypad.illuminate(5, 255, 0, 0)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(5, 0, 0, 0)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(5, 255, 0, 0)
    keypad.update()
    
    for i in range (0, 1):
        keypad.illuminate(6, 0, 255, 0)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(6, 0, 0, 0)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(6, 0, 255, 0)
    keypad.update()
    
    while keypressed != 32 or keypressed != 64:
        keypressed = keypad.get_button_states()
        if keypressed == 64:
            stay_in = 1
            break
        elif keypressed == 32:
            stay_in = 0
            break
    if stay_in == 0:
        break
    if stay_in == 1:
        gottem = 1
        stay_in = 0
        clear_board()
        rgb = []
        rgb_numb = []
        last_button_states = 0
        memory = []
        number_of_items = 0
        show_button_speed = 1
        keypad.illuminate(5, 0, 0, 0)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(6, 0, 0, 0)
        keypad.update()
        SPPED = 0
        Normal = 0
        Godlike = 0
        
keypad.illuminate(5, 0, 0, 0)
keypad.update()
time.sleep(0.1)
keypad.illuminate(6, 0, 0, 0)
keypad.update()         
