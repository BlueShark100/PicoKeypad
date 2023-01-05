import time
import picokeypad as keypad
import random
from machine import Pin
import _thread

keypad.init()
keypad.set_brightness(1.0)

line = []
line_ = []

def clear_board():
    for i in range(0, 16):
        keypad.illuminate(i, 0, 0, 0)
    keypad.update()

wait_time = random.randint(7, 100)

row_ = 0

keypressed = keypad.get_button_states()

go_down = random.randint(0, 2)
mode = random.randint(0, 3)
start_pos1 = random.randint(1, 3)
start_pos2 = random.randint(0, 2)
flipit = random.randint(0,1)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

matrix = [[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
          [12, 13, 14, 15]]

saver = random.randint(0, 15)
keypressed = keypad.get_button_states()
saverleave = 0
saver_last = 0

for i in range (0, 16):
    keypad.illuminate(i, 0, 0, 0)
keypad.update()

last_button_states = 0

keypad.illuminate(0, 0, 0, 255)
keypad.illuminate(3, 255, 0, 0)
keypad.update()

while True:
    keypressed = keypad.get_button_states()
    if saverleave == 1:
        break
    if last_button_states != keypressed:
        if saverleave == 1:
            break
        last_button_states = keypressed
        if keypressed > 0:
            if saverleave == 1:
                break
            elif keypressed == 1:
                clear_board()
                time.sleep(0.1)
                while True:
                    for i in range (0, 4):
                        saver = random.randint(0, 15)
                        if saver_last == saver:
                            saver = random.randint(0, 15)
                        r = random.randint(0, 255)
                        g = random.randint(0, 255)
                        b = random.randint(0, 255)
                        keypad.illuminate(saver, r, g, b)
                        keypad.update()
                        time.sleep(0)
                        keypressed = keypad.get_button_states()
                        saver_last = saver
                        if keypressed > 0:
                            saverleave = 1
                            break
                    if saverleave == 1:
                        break
                    for i in range (0, 100):
                        time.sleep(0.01)
                        keypressed = keypad.get_button_states()
                        if keypressed > 0:
                            saverleave = 1
                            break
                    if saverleave == 1:
                        break
                    clear_board()
                    
                for i in range (0, 16):
                    keypad.illuminate(i, 0, 0, 0)
                    keypad.update()
                    time.sleep(0.05)
            elif keypressed == 8:
                clear_board()
                time.sleep(0.1)
                while True:
                    if mode == 0:
                        for i in range (start_pos2, 4, 1):
                            line = matrix[row_]
                            line_.append(line[i])
                            if go_down == 0:
                                row_ = row_
                            elif go_down == 1:
                                row_ = row_ + 1
                            elif go_down == 2 and i > start_pos1 and row_ > 3:
                                row_ = row_ + 1
                                line = matrix[row_]
                                line_.append(line[i])
                            go_down = random.randint(0, 2)
                    elif mode == 1:   
                        for i in range (start_pos1, -1, -1):
                            line = matrix[row_]
                            line_.append(line[i])
                            if go_down == 0:
                                row_ = row_
                            elif go_down == 1:
                                row_ = row_ + 1
                            elif go_down == 2 and i > start_pos1 and row_ > 3:
                                row_ = row_ - 1
                                line = matrix[row_]
                                line_.append(line[i])
                            go_down = random.randint(0, 2)
                    elif mode == 2:
                        for i in range (start_pos2, 4, 1):
                            line = matrix[i]
                            line_.append(line[row_])
                            if go_down == 0:
                                row_ = row_
                            elif go_down == 1:
                                row_ = row_ + 1
                            elif go_down == 2 and i > start_pos1 and row_ > 3:
                                row_ = row_ + 1
                                line = matrix[row_]
                                line_.append(line[i])
                            go_down = random.randint(0, 2)
                    elif mode == 3:
                        for i in range (start_pos1, -1, -1):
                            line = matrix[i]
                            line_.append(line[row_])
                            if go_down == 0:
                                row_ = row_
                            elif go_down == 1:
                                row_ = row_ + 1
                            elif go_down == 2 and i > start_pos1 and row_ > 3:
                                row_ = row_ - 1
                                line = matrix[row_]
                                line_.append(line[i])
                            go_down = random.randint(0, 2)
                            
                    if flipit == 1:
                        line_.reverse()
                    
                    for i in range(0, len(line_) + 2):
                        if i == len(line_) + 1:
                            keypad.illuminate(line_[len(line_) - 1], 0, 0, 0)
                        elif i == len(line_):
                            keypad.illuminate(line_[len(line_) - 2], 0, 0, 0)
                        elif i == 0 or i == 1:
                            keypad.illuminate(line_[i], r, g, b)
                        else:
                            keypad.illuminate(line_[i], r, g, b)
                            keypad.illuminate(line_[i - 2], 0, 0, 0)
                        keypad.update()
                        keypressed = keypad.get_button_states()
                        if keypressed > 0:
                            saverleave = 1
                            break
                        time.sleep(0.04)
                    keypressed = keypad.get_button_states()
                    if keypressed > 0:
                        saverleave = 1
                        break
                    for i in range(wait_time, -1, -1):
                        time.sleep(0.01)
                    row_ = 0
                    line = []
                    line_ = []
                    wait_time = random.randint(0, 1)
                    mode = random.randint(0, 3)
                    go_down = random.randint(0, 2)
                    start_pos1 = random.randint(1, 3)
                    start_pos2 = random.randint(0, 2)
                    flipit = random.randint(0,1)
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    while r != 255 or g != 255 or b != 255:
                        r = r + 1
                        if r > 250:
                            break
                        g = g + 1
                        if g > 250:
                            break
                        b = b + 1
                        if b > 250:
                            break
clear_board()
                



