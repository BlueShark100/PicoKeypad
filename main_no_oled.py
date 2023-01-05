import board
import time
import picokeypad as keypad
import random
from machine import Pin
import _thread

keypad.init()
keypad.set_brightness(1.0)

openspeed = 0.07

welcometext = 0.07
up = 31
down = 32
close = 128
    
passed = 0

back = 0

last_button_states = 0

led = Pin(25, Pin.OUT)

def clear_board():
    for i in range(0, 16):
        keypad.illuminate(i, 0, 0, 0)

led.value(1)
clear_board()
keypad.update()

while True:
    keypressed = keypad.get_button_states()
    if last_button_states != keypressed:
        last_button_states = keypressed
        if keypressed > 0:
            while keypressed == 8192:
                keypad.illuminate(1, 0, 255, 0)
                keypad.update()
                led.value(0)
                while keypressed != 512:
                    keypressed = keypad.get_button_states()
                keypad.illuminate(5, 0, 255, 0)
                keypad.update()
                while keypressed != 256:
                    keypressed = keypad.get_button_states()
                keypad.illuminate(4, 0, 255, 0)
                keypad.update()
                while keypressed != 4:
                    keypressed = keypad.get_button_states()
                keypad.illuminate(14, 0, 0, 255)
                keypad.update()
                while keypressed != 64:
                    keypressed = keypad.get_button_states()
                keypad.illuminate(10, 0, 0, 255)
                keypad.update()
                while keypressed != 128:
                    keypressed = keypad.get_button_states()
                keypad.illuminate(11, 0, 0, 255)
                keypad.update()
                passed = 1
                break
            if passed == 1:
                break



print("-= pog moment detected =-")
print("Awating Initialization...")
print("")

while keypressed != 576:
    keypressed = keypad.get_button_states()

#center row
keypad.illuminate(3, 255, 255, 255)
keypad.illuminate(6, 255, 255, 255)
keypad.illuminate(9, 255, 255, 255)
keypad.illuminate(12, 255, 255, 255)
keypad.update()

time.sleep(openspeed)
#2nd row down
keypad.illuminate(7, 255, 255, 255)
keypad.illuminate(10, 255, 255, 255)
keypad.illuminate(13, 255, 255, 255)

#2nd row up
keypad.illuminate(2, 255, 255, 255)
keypad.illuminate(5, 255, 255, 255)
keypad.illuminate(8, 255, 255, 255)

#center row off
keypad.illuminate(3, 0, 0, 0)
keypad.illuminate(6, 0, 0, 0)
keypad.illuminate(9, 0, 0, 0)
keypad.illuminate(12, 0, 0, 0)

keypad.update()
time.sleep(openspeed)

#3rd row down
keypad.illuminate(11, 255, 255, 255)
keypad.illuminate(14, 255, 255, 255)

#3rd row up
keypad.illuminate(1, 255, 255, 255)
keypad.illuminate(4, 255, 255, 255)

#2nd row down off
keypad.illuminate(7, 0, 0, 0)
keypad.illuminate(10, 0, 0, 0)
keypad.illuminate(13, 0, 0, 0)

#2nd row up off
keypad.illuminate(2, 0, 0, 0)
keypad.illuminate(5, 0, 0, 0)
keypad.illuminate(8, 0, 0, 0)
keypad.update()

time.sleep(openspeed)

#4th row down
keypad.illuminate(15, 255, 255, 255)
#4th row up
keypad.illuminate(0, 255, 255, 255)

#3rd row down off
keypad.illuminate(11, 0, 0, 0)
keypad.illuminate(14, 0, 0, 0)

#3rd row up off
keypad.illuminate(1, 0, 0, 0)
keypad.illuminate(4, 0, 0, 0)
keypad.update()

time.sleep(openspeed)

#4th rows off
keypad.illuminate(0, 0, 0, 0)
keypad.illuminate(15, 0, 0, 0)
keypad.update()

time.sleep(0.2)

for i in range(0, 2):
    keypad.illuminate(0, 10, 255, 10)
    keypad.update()
    time.sleep(0.15)
    keypad.illuminate(0, 0, 0, 0)
    keypad.update()
    time.sleep(0.15)
    
    
time.sleep(0.3)

print("-------")
print("Welcome")
print("-------")
print("")


for l in range(0,28): #clears the board
    if l < 16:
        keypad.illuminate(l, 2, 2, 5)
    if l < 17:
        if l > 0:
            keypad.illuminate(l-1, 5, 5, 15)
    if l < 18:
        if l > 1:
            keypad.illuminate(l-2, 10, 10, 25)
    if l < 19:
        if l > 2:
            keypad.illuminate(l-3, 15, 15, 30)
    if l < 20:
        if l > 3:
            keypad.illuminate(l-4, 20, 20, 35)
    if l < 21:
        if l > 4:
            keypad.illuminate(l-5, 25, 25, 45)
    if l < 22:
        if l > 5:
            keypad.illuminate(l-6, 30, 30, 55)
    if l < 23:
        if l > 6:
            keypad.illuminate(l-7, 35, 35, 60)
    if l < 24:
        if l > 7:
            keypad.illuminate(l-8, 40, 40, 65)
    if l < 25:
        if l > 8:
            keypad.illuminate(l-9, 45, 45, 70)
    if l < 26:
        if l > 9:
            keypad.illuminate(l-10, 50, 50, 75)
    if l < 27:
        if l > 10:
            keypad.illuminate(l-11, 55, 55, 80)
    time.sleep(0.06)
    keypad.update()

for i in range (0, 1):
    keypad.illuminate(0, 0, 255, 0)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(0, 55, 55, 80)
    keypad.update()
    time.sleep(0.1)
keypad.illuminate(0, 0, 255, 0)
keypad.update()

for i in range (0, 1):
    keypad.illuminate(1, 30, 30, 255)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(1, 55, 55, 80)
    keypad.update()
    time.sleep(0.1)
keypad.illuminate(1, 30, 30, 255)
keypad.update()

for i in range (0, 1):
    keypad.illuminate(2, 255, 0, 255)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(2, 55, 55, 80)
    keypad.update()
    time.sleep(0.1)
keypad.illuminate(2, 255, 0, 255)
keypad.update()

for i in range (0, 1):
    keypad.illuminate(3, 255, 0, 0)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(3, 55, 55, 80)
    keypad.update()
    time.sleep(0.1)
keypad.illuminate(3, 255, 0, 0)
keypad.update()

while True:
    keypressed = keypad.get_button_states()
    if last_button_states != keypressed:
        last_button_states = keypressed
        if keypressed > 0:
            if keypressed == 1:
                print("")
                print("Entering: Whack-A-Mole")
                print("")
                speed = 1.5
                wait_time = 0
                themole = random.randint(0, 15)
                gottem = 0
                score = 0

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                keypressed = keypad.get_button_states()

                def clear_board():
                    for i in range(0, 16):
                        keypad.illuminate(i, 0, 0, 0)
                    keypad.update()

                while True:
                    for i in range(0,16):
                        keypad.illuminate(i, 255, 0, 0)
                        keypad.update()
                        time.sleep(0.01)
                    time.sleep(0.55)
                    for i in range(0,16):
                        keypad.illuminate(i, 255, 255, 0)
                        keypad.update()
                        time.sleep(0.01)
                    time.sleep(0.55)
                    for i in range(0,16):
                        keypad.illuminate(i, 0, 255, 0)
                        keypad.update()
                        time.sleep(0.01)
                    time.sleep(0.55)
                    clear_board()
                    while True:
                        r = random.randint(0, 255)
                        g = random.randint(0, 255)
                        b = random.randint(0, 255)
                        themole = random.randint(0, 15)
                        keypad.illuminate(themole, r, g, b)
                        keypad.update()
                        while True:
                            keypressed = keypad.get_button_states()
                            if keypressed == 0:
                                keypressed = 0.5
                            elif keypressed == 1: #0 translates the value to a more usable number
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

                            if score == 8:
                                speed = 1.2
                            elif score == 20:
                                speed = 0.8
                            elif score == 30:
                                speed = 0.7
                            elif score == 45:
                                speed = 0.6
                            elif score == 60:
                                speed = 0.55
                            
                            if keypressed == themole and gottem == 0:
                                clear_board()
                                keypad.update()
                                gottem = 1
                                score = score + 1
                            time.sleep(0.01)
                            wait_time = wait_time + 0.01
                            if wait_time > speed:
                                break
                        if gottem == 0:
                            break
                        wait_time = 0
                        gottem = 0
                        
                    for i in range(0,16):
                        keypad.illuminate(i, 255, 0, 0)
                        keypad.update()
                        time.sleep(0.01)
                        
                    for i in range(0,16):
                        keypad.illuminate(i, 0, 0, 0)
                        keypad.update()
                        time.sleep(0.01)
                        
                    print("---------")
                    print("Good Game")
                    print("Score:", score)
                    print("---------")
                    
                    time.sleep(0.45)
                    
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
                    speed = 1.5
                    wait_time = 0
                    themole = random.randint(0, 15)
                    gottem = 0
                    score = 0
                    keypad.illuminate(5, 0, 0, 0)
                    keypad.update()
                    time.sleep(0.1)
                    keypad.illuminate(6, 0, 0, 0)
                    keypad.update()
                    
                    if stay_in == 0:
                        break
                    time.sleep(0.6)
                back = 1
            
            if keypressed == 2: # Matrix Man
                print("")
                print("Entering: Matrix Man")
                print("")
                button_states = keypad.get_button_states()
                last_button_states = 0


                NUM_PADS = keypad.get_num_pads()

                column_ = 0
                row_ = 0

                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)

                keypressed = 5

                matrix = [[0, 1, 2, 3],
                          [4, 5, 6, 7],
                          [8, 9, 10, 11],
                          [12, 13, 14, 15]]

                on = 255
                open_speed = 0.05

                keypad.illuminate(1, 0, 0, 255)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(0, on, on, on)
                keypad.illuminate(2, on, on, on)
                keypad.illuminate(5, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(4, on, on, on)
                keypad.illuminate(9, on, on, on)
                keypad.illuminate(6, on, on, on)
                keypad.illuminate(3, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(8, on, on, on)
                keypad.illuminate(13, on, on, on)
                keypad.illuminate(10, on, on, on)
                keypad.illuminate(7, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(12, on, on, on)
                keypad.illuminate(14, on, on, on)
                keypad.illuminate(11, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(15, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                on = 0

                keypad.illuminate(1, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(0, on, on, on)
                keypad.illuminate(2, on, on, on)
                keypad.illuminate(5, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(4, on, on, on)
                keypad.illuminate(9, on, on, on)
                keypad.illuminate(6, on, on, on)
                keypad.illuminate(3, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(8, on, on, on)
                keypad.illuminate(13, on, on, on)
                keypad.illuminate(10, on, on, on)
                keypad.illuminate(7, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(12, on, on, on)
                keypad.illuminate(14, on, on, on)
                keypad.illuminate(11, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(15, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                leavematrix = 0

                while True:
                    if leavematrix == 1:
                        break
                    keypressed = keypad.get_button_states()
                    if last_button_states != keypressed:
                        last_button_states = keypressed
                        if keypressed > 0:
                            r = random.randint(0,255)
                            g = random.randint(0,255)
                            b = random.randint(0,255)
                            
                            if keypressed == 32769:
                                leavematrix = 1
                                break
                            elif keypressed == 1: #0   #sets the correct column and row for the key pressed, I brute forced it
                                column_ = 0
                                row_ = 0
                            elif keypressed == 2: #1
                                column_ = 1
                                row_ = 0
                            elif keypressed == 4: #2
                                column_ = 2
                                row_ = 0
                            elif keypressed == 8: #3
                                column_ = 3
                                row_ = 0
                            elif keypressed == 16: #4
                                column_ = 0
                                row_ = 1
                            elif keypressed == 32: #5
                                column_ = 1
                                row_ = 1
                            elif keypressed == 64: #6
                                column_ = 2
                                row_ = 1
                            elif keypressed == 128: #7
                                column_ = 3
                                row_ = 1
                            elif keypressed == 256: #8
                                column_ = 0
                                row_ = 2
                            elif keypressed == 512: #9
                                column_ = 1
                                row_ = 2
                            elif keypressed == 1024: #A
                                column_ = 2
                                row_ = 2
                            elif keypressed == 2048: #B
                                column_ = 3
                                row_ = 2
                            elif keypressed == 4096: #C
                                column_ = 0
                                row_ = 3
                            elif keypressed == 8192: #D
                                column_ = 1
                                row_ = 3
                            elif keypressed == 16384: #E
                                column_ = 2
                                row_ = 3
                            elif keypressed == 32768: #F
                                column_ = 3
                                row_ = 3
                                
                            row = matrix[row_] #makes the row selected (row_) an actual list 

                            column = []
                            for p in matrix:  
                              column.append(p[column_]) #adds the values of the specifies number (column_) in each row to an empty list to make a column

                            for i in range(0,16): #clears the board
                                keypad.illuminate(i, 0, 0, 0)
                            keypad.update()
                            for i in range(0,4): #make the cross
                                keypad.illuminate(column[i], r, g, b)
                                keypad.illuminate(row[i], r, g, b)
                                keypad.update()
                                time.sleep(0)
                on = 255
                open_speed = 0.07

                keypad.illuminate(15, on, on, on)
                keypad.illuminate(0, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(11, on, on, on)
                keypad.illuminate(14, on, on, on)
                keypad.illuminate(1, on, on, on)
                keypad.illuminate(4, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(7, on, on, on)
                keypad.illuminate(10, on, on, on)
                keypad.illuminate(13, on, on, on)
                keypad.illuminate(2, on, on, on)
                keypad.illuminate(5, on, on, on)
                keypad.illuminate(8, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(3, on, on, on)
                keypad.illuminate(6, on, on, on)
                keypad.illuminate(9, on, on, on)
                keypad.illuminate(12, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                on = 0

                keypad.illuminate(15, on, on, on)
                keypad.illuminate(0, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(11, on, on, on)
                keypad.illuminate(14, on, on, on)
                keypad.illuminate(1, on, on, on)
                keypad.illuminate(4, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(7, on, on, on)
                keypad.illuminate(10, on, on, on)
                keypad.illuminate(13, on, on, on)
                keypad.illuminate(2, on, on, on)
                keypad.illuminate(5, on, on, on)
                keypad.illuminate(8, on, on, on)
                keypad.update()
                time.sleep(open_speed)

                keypad.illuminate(3, on, on, on)
                keypad.illuminate(6, on, on, on)
                keypad.illuminate(9, on, on, on)
                keypad.illuminate(12, on, on, on)
                keypad.update()
                time.sleep(open_speed)
                back = 1
            
            if keypressed == 8:
                print("")
                print("Entering: Screen Saver")
                print("")
                time.sleep(0.1)
                line = []
                line_ = []

                def clear_board():
                    for i in range(0, 16):
                        keypad.illuminate(i, 0, 0, 0)
                    keypad.update()

                wait_time = random.randint(7, 130)

                row_ = 0

                keypressed = keypad.get_button_states()

                go_down = random.randint(0, 2)
                mode = random.randint(0, 3)
                start_pos1 = random.randint(1, 3)
                start_pos2 = random.randint(0, 2)
                flipit = random.randint(0,1)
                r = random.randint(0, 250)
                g = random.randint(0, 250)
                b = random.randint(0, 250)

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
                                        keypressed = keypad.get_button_states()
                                        if keypressed > 0:
                                            saverleave = 1
                                            break
                                    row_ = 0
                                    line = []
                                    line_ = []
                                    wait_time = random.randint(7, 200)
                                    mode = random.randint(0, 3)
                                    go_down = random.randint(0, 2)
                                    start_pos1 = random.randint(1, 3)
                                    start_pos2 = random.randint(0, 2)
                                    flipit = random.randint(0,1)
                                    r = random.randint(0, 255)
                                    g = random.randint(0, 255)
                                    b = random.randint(0, 255)
                                    while True:
                                        if r > 250:
                                            break
                                        r = r + 1
                                        if g > 250:
                                            break
                                        g = g + 1
                                        if b > 250:
                                            break
                                        b = b + 1
                clear_board()
                saverleave = 0
                time.sleep(0.5)
                back = 1
            
            if keypressed == 4:
                print("")
                print("Entering: Memory")
                print("")
                keypressed = keypad.get_button_states()

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
                                    Normal = 1
                                elif keypressed == 64:
                                    print("SPEED")
                                    SPPED = 1
                                elif keypressed == 256:
                                    print("=== WARP SPEED ===")
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
                back = 1
            if keypressed == 16:
                print("4")
            if keypressed == 32:
                print("5")
            if keypressed == 64:
                print("6")
            if keypressed == 128:
                print("7")
            if keypressed == 256:
                print("8")
            if keypressed == 512:
                print("9")
            if keypressed == 1024:
                print("A")
            if keypressed == 2048:
                print("B")
            if keypressed == 4096:
                print("C")
            if keypressed == 8192:
                print("D")
            if keypressed == 16384:
                print("E")
            if keypressed == 32768:
                print("F")
                
            if back == 1:
                print("------------")
                print("Welcome back")
                print("------------")
                for l in range(0,28): #clears the board
                    if l < 16:
                        keypad.illuminate(l, 2, 2, 5)
                    if l < 17:
                        if l > 0:
                            keypad.illuminate(l-1, 5, 5, 15)
                    if l < 18:
                        if l > 1:
                            keypad.illuminate(l-2, 10, 10, 25)
                    if l < 19:
                        if l > 2:
                            keypad.illuminate(l-3, 15, 15, 30)
                    if l < 20:
                        if l > 3:
                            keypad.illuminate(l-4, 20, 20, 35)
                    if l < 21:
                        if l > 4:
                            keypad.illuminate(l-5, 25, 25, 45)
                    if l < 22:
                        if l > 5:
                            keypad.illuminate(l-6, 30, 30, 55)
                    if l < 23:
                        if l > 6:
                            keypad.illuminate(l-7, 35, 35, 60)
                    if l < 24:
                        if l > 7:
                            keypad.illuminate(l-8, 40, 40, 65)
                    if l < 25:
                        if l > 8:
                            keypad.illuminate(l-9, 45, 45, 70)
                    if l < 26:
                        if l > 9:
                            keypad.illuminate(l-10, 50, 50, 75)
                    if l < 27:
                        if l > 10:
                            keypad.illuminate(l-11, 55, 55, 80)
                    time.sleep(0.06)
                    keypad.update()
                for i in range (0, 1):
                    keypad.illuminate(0, 0, 255, 0)
                    keypad.update()
                    time.sleep(0.1)
                    keypad.illuminate(0, 55, 55, 80)
                    keypad.update()
                    time.sleep(0.1)
                keypad.illuminate(0, 0, 255, 0)
                keypad.update()
                for i in range (0, 1):
                    keypad.illuminate(1, 30, 0, 255)
                    keypad.update()
                    time.sleep(0.1)
                    keypad.illuminate(1, 55, 55, 80)
                    keypad.update()
                    time.sleep(0.1)
                keypad.illuminate(1, 30, 30, 255)
                keypad.update()
                for i in range (0, 1):
                    keypad.illuminate(2, 255, 0, 255)
                    keypad.update()
                    time.sleep(0.1)
                    keypad.illuminate(2, 55, 55, 80)
                    keypad.update()
                    time.sleep(0.1)
                keypad.illuminate(2, 255, 0, 255)
                keypad.update()
                for i in range (0, 1):
                    keypad.illuminate(3, 255, 0, 0)
                    keypad.update()
                    time.sleep(0.1)
                    keypad.illuminate(3, 55, 55, 80)
                    keypad.update()
                    time.sleep(0.1)
                keypad.illuminate(3, 255, 0, 0)
                keypad.update()
                
                back = 0

