from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import picokeypad as keypad
import _thread
import framebuf
import random

keypad.init()
keypad.set_brightness(1)

def wipe_out(): #wipes the contec on the displays quikly per character from right to left
    rect_loc = 128
    for i in range(0, 129, 8):
        oled.fill_rect(rect_loc, 0, i, 64, 0)
        oled2.fill_rect(rect_loc, 0, i, 64, 0)
        oled.show()
        oled2.show()
        rect_loc = rect_loc - 8

def screen_saver_boi(): #define the 1980s movie computer screen saver as a boi
    time.sleep(0.5)
    clear_board()
    global saverleave
    saverleave = 0
    while True:
        dem_four = []
        while len(dem_four) != 4:
            saver = random.randint(0, 15)
            if saver in dem_four:
                time.sleep(0)
            else:
                dem_four.append(saver)
        for i in range (0, 4):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            keypad.illuminate(dem_four[i], r, g, b)
            keypad.update()
            keypressed = keypad.get_button_states()
            if keypressed > 0:
                saverleave = 1
                break
        if saverleave == 1:
            break
        for i in range (0, 130):
            time.sleep(0.01)
            keypressed = keypad.get_button_states()
            if keypressed > 0:
                saverleave = 1
                break
        if saverleave == 1:
            break
        clear_board()
    clear_board()

def screen_saver_lad(): #define the lighting screen saver as a lad
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

def enter_wackamole(): 
    wipe_out()
    oled.text("-= Entering =-", 9, 20)
    oled.text("Whack-A-Mole", 17, 30)
    oled.show()
    time.sleep(2.2)
    oled.fill(0)
    oled.show()

#start defining byte arrays for the big numbers
zero_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x0f\xff\x80\x00\x00\x7f\xff\xf8\x00\x01\xff\xff\xfe\x00\x03\xff\xff\xff\x00\x07\xff\xff\xff\x80\x0f\xff\xff\xff\xc0\x0f\xff\xff\xff\xc0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\x87\xff\xe0\x1f\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x1f\xff\x87\xff\xf0\x1f\xff\x87\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x0f\xff\xff\xff\xc0\x07\xff\xff\xff\xc0\x07\xff\xff\xff\x80\x03\xff\xff\xff\x00\x01\xff\xff\xfe\x00\x00\x7f\xff\xf8\x00\x00\x0f\xff\xc0\x00\x00\x00\x00\x00\x00')
zero_number = framebuf.FrameBuffer(zero_buffer, 36, 58, framebuf.MONO_HLSB)
    
one_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfc\x00\x00\x00\x0f\xfc\x00\x00\x00\x1f\xfc\x00\x00\x00?\xfc\x00\x00\x00\xff\xfc\x00\x00\x01\xff\xfc\x00\x00\x07\xff\xfc\x00\x00\x7f\xff\xfc\x00\x03\xff\xff\xfc\x00\x03\xff\xff\xfc\x00\x03\xff\xff\xfc\x00\x03\xff\xff\xfc\x00\x03\xff\xff\xfc\x00\x03\xff\xff\xfc\x00\x00\x0f\xff\xfc\x00\x00\x03\xff\xfc\x00\x00\x01\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\xff\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
one_number = framebuf.FrameBuffer(one_buffer, 36, 58, framebuf.MONO_HLSB)

two_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x0f\xff\xc0\x00\x00\x7f\xff\xf8\x00\x01\xff\xff\xfc\x00\x03\xff\xff\xff\x00\x07\xff\xff\xff\x00\x07\xff\xff\xff\x80\x0f\xff\xff\xff\xc0\x0f\xff\xff\xff\xc0\x1f\xff\xff\xff\xe0\x1f\xff\x87\xff\xe0\x1f\xff\x07\xff\xe0\x1f\xff\x07\xff\xe0?\xff\x07\xff\xf0?\xff\x07\xff\xf0?\xff\x07\xff\xf0?\xff\x07\xff\xe0?\xff\x0f\xff\xe0?\xff\x0f\xff\xe0?\xff\x1f\xff\xe0\x00\x00\x1f\xff\xe0\x00\x00?\xff\xc0\x00\x00?\xff\xc0\x00\x00\x7f\xff\xc0\x00\x00\x7f\xff\x80\x00\x00\xff\xff\x80\x00\x00\xff\xff\x00\x00\x01\xff\xff\x00\x00\x01\xff\xfe\x00\x00\x03\xff\xfe\x00\x00\x07\xff\xfc\x00\x00\x07\xff\xf8\x00\x00\x0f\xff\xf8\x00\x00\x0f\xff\xe0\x00\x00\x1f\xff\xe0\x00\x00\x7f\xff\xc0\x00\x00\x7f\xff\x80\x00\x00\xff\xff\x80\x00\x00\xff\xff\x00\x00\x01\xff\xfe\x00\x00\x03\xff\xfe\x00\x00\x03\xff\xfc\x00\x00\x07\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x0f\xff\xf0\x00\x00\x1f\xff\xff\xff\xc0\x1f\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
two_number = framebuf.FrameBuffer(two_buffer, 36, 58, framebuf.MONO_HLSB)

three_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xff\x00\x00\x01\xff\xff\xe0\x00\x03\xff\xff\xfc\x00\x07\xff\xff\xfe\x00\x0f\xff\xff\xff\x00\x1f\xff\xff\xff\x80\x1f\xff\xff\xff\x80\x1f\xff\xff\xff\xc0?\xff\x8f\xff\xc0?\xff\x07\xff\xc0?\xff\x07\xff\xc0?\xff\x07\xff\xc0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xc0?\xff\x07\xff\xc0\x00\x00\x07\xff\xc0\x00\x00\x07\xff\xc0\x00\x00\x07\xff\xc0\x00\x00\x0f\xff\x80\x00\x07\xff\xff\x00\x00\x07\xff\xfe\x00\x00\x07\xff\xfc\x00\x00\x07\xff\xfc\x00\x00\x07\xff\xff\x00\x00\x07\xff\xff\x80\x00\x07\xff\xff\xc0\x00\x07\xff\xff\xc0\x00\x00\x1f\xff\xc0\x00\x00\x0f\xff\xe0\x00\x00\x0f\xff\xe0\x00\x00\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0?\xff\x07\xff\xe0\x1f\xff\x07\xff\xe0\x1f\xff\x07\xff\xc0\x1f\xff\x8f\xff\xc0\x1f\xff\xff\xff\xc0\x0f\xff\xff\xff\x80\x0f\xff\xff\xff\x80\x07\xff\xff\xff\x00\x03\xff\xff\xfe\x00\x01\xff\xff\xfc\x00\x00\x1f\xff\xe0\x00\x00\x03\xfe\x00\x00\x00\x00\x00\x00\x00')
three_number = framebuf.FrameBuffer(three_buffer, 36, 58, framebuf.MONO_HLSB)

four_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xff\x80\x00\x07\xff\xff\x80\x00\x07\xff\xff\x80\x00\x0f\xff\xff\x80\x00\x0f\xff\xff\x80\x00\x0f\xff\xff\x80\x00\x1f\xff\xff\x80\x00\x1f\xff\xff\x80\x00\x1f\xff\xff\x80\x00\x1f\xff\xff\x80\x00\x7f\xff\xff\x80\x00\x7f\xff\xff\x80\x00\xff\xff\xff\x80\x00\xff\xff\xff\x80\x00\xff\xff\xff\x80\x00\xff\xff\xff\x80\x01\xff\xff\xff\x80\x01\xff\xbf\xff\x80\x01\xff\xbf\xff\x80\x03\xff\xbf\xff\x80\x03\xff\xbf\xff\x80\x03\xff?\xff\x80\x07\xff?\xff\x80\x07\xff?\xff\x80\x07\xff?\xff\x80\x0f\xfe?\xff\x80\x0f\xfe?\xff\x80\x0f\xfe?\xff\x80\x1f\xfe?\xff\x80\x1f\xfc?\xff\x80\x1f\xfc?\xff\x80?\xfc?\xff\x80?\xfc?\xff\x80?\xf8?\xff\x80\x7f\xf8?\xff\x80\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x7f\xff\xff\xff\xf8\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
four_number = framebuf.FrameBuffer(four_buffer, 36, 58, framebuf.MONO_HLSB)

five_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xff\xff\xff\x80?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\xff\xff\xc0?\xff\x00\x00\x00?\xff\x00\x00\x00?\xff\x00\x00\x00?\xff\x00\x00\x00?\xff\x03\x80\x00?\xff\x1f\xfc\x00?\xff\x7f\xff\x00?\xff\xff\xff\x80?\xff\xff\xff\xc0?\xff\xff\xff\xe0?\xff\xff\xff\xe0?\xff\xff\xff\xe0?\xff\xff\xff\xf0?\xff\xef\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x00\x00\x07\xff\xf0\x00\x00\x07\xff\xf0\x00\x00\x07\xff\xf0\x00\x00\x07\xff\xf0\x00\x00\x07\xff\xf0\x00\x00\x07\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x1f\xff\xc7\xff\xf0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x0f\xff\xff\xff\xe0\x0f\xff\xff\xff\xc0\x07\xff\xff\xff\x80\x03\xff\xff\xff\x00\x01\xff\xff\xfe\x00\x00\x7f\xff\xfc\x00\x00\x07\xff\xc0\x00\x00\x00\x00\x00\x00')
five_number = framebuf.FrameBuffer(five_buffer, 36, 58, framebuf.MONO_HLSB)

six_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x0f\xff\xe0\x00\x00\x7f\xff\xfc\x00\x01\xff\xff\xff\x00\x03\xff\xff\xff\x80\x07\xff\xff\xff\xc0\x0f\xff\xff\xff\xc0\x0f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xf0\x1f\xff\xc7\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x80\x00\x00?\xff\x87\xf8\x00?\xff\x9f\xfe\x00?\xff\xff\xff\x80?\xff\xff\xff\xc0?\xff\xff\xff\xe0?\xff\xff\xff\xe0?\xff\xff\xff\xf0?\xff\xff\xff\xf0?\xff\xff\xff\xf0?\xff\xcf\xff\xf0?\xff\xc7\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x1f\xff\xc7\xff\xf0\x1f\xff\xff\xff\xf0\x1f\xff\xff\xff\xf0\x0f\xff\xff\xff\xe0\x0f\xff\xff\xff\xc0\x07\xff\xff\xff\xc0\x03\xff\xff\xff\x80\x01\xff\xff\xff\x00\x00\x7f\xff\xfc\x00\x00\x07\xff\xe0\x00\x00\x00\x00\x00\x00')
six_number = framebuf.FrameBuffer(six_buffer, 36, 58, framebuf.MONO_HLSB)

seven_buffer = bytearray(b'\x00\x00\x00\x00\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x1f\xff\xff\xff\x00\x00\x00\x7f\xff\x00\x00\x00\x7f\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfc\x00\x00\x03\xff\xfc\x00\x00\x03\xff\xfc\x00\x00\x03\xff\xfc\x00\x00\x03\xff\xfc\x00\x00\x03\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x0f\xff\xe0\x00\x00\x0f\xff\xe0\x00\x00\x0f\xff\xe0\x00\x00\x0f\xff\xe0\x00\x00\x0f\xff\xe0\x00\x00\x1f\xff\xc0\x00\x00\x1f\xff\xc0\x00\x00\x1f\xff\xc0\x00\x00\x1f\xff\xc0\x00\x00\x1f\xff\xc0\x00\x00\x7f\xff\xc0\x00\x00\x7f\xff\x80\x00\x00\x7f\xff\x80\x00\x00\x7f\xff\x80\x00\x00\x7f\xff\x80\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x00\xff\xff\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x01\xff\xfe\x00\x00\x00\x00\x00\x00\x00')
seven_number = framebuf.FrameBuffer(seven_buffer, 36, 58, framebuf.MONO_HLSB)

eight_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x0f\xff\xe0\x00\x00\xff\xff\xfc\x00\x01\xff\xff\xfe\x00\x03\xff\xff\xff\x00\x07\xff\xff\xff\x80\x0f\xff\xff\xff\xc0\x0f\xff\xff\xff\xc0\x1f\xff\xff\xff\xe0\x1f\xff\xcf\xff\xe0\x1f\xff\x87\xff\xe0?\xff\x87\xff\xe0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xe0\x1f\xff\x87\xff\xe0\x1f\xff\x87\xff\xe0\x1f\xff\xcf\xff\xe0\x0f\xff\xff\xff\xc0\x0f\xff\xff\xff\x80\x07\xff\xff\xff\x00\x03\xff\xff\xfe\x00\x03\xff\xff\xff\x00\x07\xff\xff\xff\x80\x0f\xff\xff\xff\xc0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0?\xff\xcf\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x0f\xff\xff\xff\xc0\x07\xff\xff\xff\x80\x03\xff\xff\xff\x00\x01\xff\xff\xfe\x00\x00\x7f\xff\xfc\x00\x00\x0f\xff\xc0\x00\x00\x00\x00\x00\x00')
eight_number = framebuf.FrameBuffer(eight_buffer, 36, 58, framebuf.MONO_HLSB)

nine_buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x1f\xff\xe0\x00\x00\xff\xff\xfc\x00\x01\xff\xff\xff\x00\x03\xff\xff\xff\x80\x07\xff\xff\xff\xc0\x0f\xff\xff\xff\xc0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xe0\x1f\xff\xff\xff\xf0?\xff\xc7\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\xc7\xff\xf8?\xff\xef\xff\xf8?\xff\xff\xff\xf8\x1f\xff\xff\xff\xf8\x1f\xff\xff\xff\xf8\x1f\xff\xff\xff\xf8\x0f\xff\xff\xff\xf8\x07\xff\xff\xff\xf8\x03\xff\xff\xff\xf8\x00\xff\xf7\xff\xf8\x00\x1f\x87\xff\xf8\x00\x00\x07\xff\xf8\x00\x00\x07\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf8?\xff\x87\xff\xf0?\xff\x87\xff\xf0?\xff\x87\xff\xf0\x1f\xff\xc7\xff\xf0\x1f\xff\xff\xff\xf0\x1f\xff\xff\xff\xe0\x0f\xff\xff\xff\xe0\x0f\xff\xff\xff\xc0\x07\xff\xff\xff\x80\x03\xff\xff\xff\x00\x01\xff\xff\xfe\x00\x00\x7f\xff\xfc\x00\x00\x0f\xff\xc0\x00\x00\x00\x00\x00\x00')
nine_number = framebuf.FrameBuffer(nine_buffer, 36, 58, framebuf.MONO_HLSB)


#loading image into a buffer so it can be refrence later (Warp Text)
warp_buffer = bytearray(b'\x03\xfe\x00\xff\x80\x03\xff\xe0\x00\xff\xff\xf0\x00\xff\xff\xe0\x04\x02\x01\x80\x80\x0c\x00\x10\x01\x80\x00\x18\x01\x00\x000\x1c\x02\x03\x00\x80\x18\x00\x08\x03\x80\x00\x0c\x03\x00\x00\x08<\x02\x07\x80\x808\x00\x08\x07\x80\x00\x04\x0f\x00\x00\x04|\x02\x1f\x00\x80x\x00\x08\x0f\x80\x00\x04\x1f\x00\x00\x04|\x02\x1f\x80\x80\xf0\x00\x04\x1f\x80\x00\x06\x1f\x00\x00\x06|\x02\x1f\x00\x80\xf0\x00\x04\x1f\x80\x00\x02\x1f\x00\x00\x02|\x02\x1f\x80\x81\xe0\x08\x04\x1f\x80x\x02\x1f\x00x\x02|\x02\x1f\x00\x81\xe0\x1c\x02\x1f\x80|\x02\x1f\x00|\x02|\x02\x7f\x80\x81\xe0\x1c\x02\x1f\x80|\x06\x1f\x00|\x02|\x02\x83\x00\x83\xc0<\x01\x1f\x80|\x04\x1f\x00|\x02|\x03\x03\x80\x83\xc0>\x01\x1f\x80x\x04\x1f\x00|\x02|\x03\x01\x00\x83\xc0>\x01\x1f\x80\x00\x0c\x1f\x00|\x02|\x03\x01\x00\x87\x80~\x01\x9f\x80\x00\x02\x1f\x00\x00\x02|\x02\x00\x80\x87\x80\x00\x00\x9f\x80\x00\x01\x1f\x00\x00\x06|\x00\x00\x00\x87\x80\x00\x00\x9f\x80\x00\x00\x9f\x00\x00\x04|\x00\x00\x00\x8f\x80\x00\x00\x9f\x80\x00\x00\x9f\x00\x00\x04|\x00\x00\x00\x8f\x80\x00\x00\x9f\x80\x00\x00\x9f\x00\x00\x08|\x00\x00\x00\x8f\x80\x00\x00\x9f\x80\x00\x00\x9f\x00\x00\x10|\x00\x10\x00\x8f\x80\x00\x00\x9f\x80\x7f\x00\x9f\x00\x00\xe0~\x000\x00\x9f\x80\x00\x00\x9f\x80\x7f\x00\x9f\x00\x7f\xc0~\x008\x00\x9f\x80\x7f\x00\x9f\x80\x7f\x00\x9f\x00\x7f\x80~\x008\x01\x1f\x80\x7f\x00\x9f\x80\x7f\x00\x9f\x00~\x00\x7f\x00x\x01\x1f\x80\x7f\x00\x9f\x80\x7f\x00\x9f\x00|\x00\x7f\x00|\x03\x1f\x80\x7f\x00\x9f\x80_\x00\x9f\x00\x00\x00\x7f\x00|\x02\x1f\x80\x7f\x00\x9f\x80_\x00\x9f\x00@\x00?\x80|\x02\x1f\x80?\x00\x9f\x80?\x00\x9f\x80\x00\x00?\xff\xff\xfc\x1f\xff\x9f\xff\x1f\xff\x9f\xff\x1f\xff\x80\x00\x1f\xfe\xff\xf0\x1f\xff?\xfe\x1f\xff\x1f\xfe\x1f\xff\x00\x00\x1f\xfc\xff\xe0\x1f\xfc?\xfc\x1f\xfc\x1f\xfc\x1f\xfc\x00\x00\x1f\xf8\x7f\xc0\x0f\xf8\x1f\xf0\x1f\xf8\x1f\xf8\x1f\xf8\x00\x00\x0f\xf0\x7f\x80\x0f\xf0\x1f\xe0\x0f\xf0\x1f\xe0\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
warp_text = framebuf.FrameBuffer(warp_buffer, 127, 33, framebuf.MONO_HLSB) 

#loading image into a buffer so it can be refrence later (Speed Text)
speed_buffer = bytearray(b"\x00\x7f\xf8\x03\xff\xf0\x00\xff\xff\x80\x7f\xff\xc0?\xff\x80\x03\x80\x04\x04\x00\x0c\x01\x00\x00@\x80\x00 @\x00p\x04\x00\x04\x0c\x00\x01\x03\x00\x00A\x80\x00 \xc0\x00\x08\x08\x00\x04\x1c\x00\x00\x87\x00\x00C\x80\x00!\xc0\x00\x04\x18\x00\x04|\x00\x00\x9f\x00\x00G\x80\x00#\xc0\x00\x020\x00\x04|\x00\x00\x9f\x00\x00O\x80\x00'\xc0\x00\x02p\x00\x04|\x00\x00_\x00\x00O\x80\x00'\xc0\x00\x02\xf0\x0f\xf8|\x07\x80_\x01\xff\x8f\x80\xff\xc7\xc0~\x02\xf0\x0f\xf0|\x07\xc0_\x01\xff\x0f\x80\xff\x87\xc0>\x02\xf0\x07\xe0|\x07\xc0_\x01\xfe\x0f\x80\xff\x07\xc0~\x02\xf0\x00\x18|\x07\xc0_\x00\x02\x0f\x80\x01\x07\xc0~\x02\xf0\x00\x04|\x07\xc0_\x00\x01\x0f\x80\x00\x87\xc0>\x02\xf8\x00\x02|\x00\x00_\x00\x01\x0f\x80\x00\x87\xc0~\x02\xf8\x00\x02|\x00\x00\x9f\x00\x01\x0f\x80\x00\x87\xc0~\x02\xfc\x00\x02|\x00\x00\x9f\x00\x01\x0f\x80\x00\x87\xc0>\x02\xff\x00\x02|\x00\x00\x9f\x00\x02\x0f\x80\x01\x07\xc0~\x02\xff\xfe\x02|\x00\x01\x1f\x01\xfc\x0f\x80\xfe\x07\xc0~\x02\xff\xfe\x02|\x00\x06\x1f\x01\xf8\x0f\x80\xfc\x07\xc0>\x02\x7f\xfe\x02|\x07\xf8\x1f\x01\xff\xcf\x80\xff\xe7\xc0|\x02\x10\x00\x02|\x07\xf0\x1f\x00\x00O\x80\x00\x07\xc0\x00\x020\x00\x02|\x07\xe0\x1f\x00\x00O\x80\x00'\xc0\x00\x02p\x00\x02|\x07\x80\x1f\x00\x00O\x80\x00\x07\xc0\x00\x06\xf0\x00\x04|\x04\x00\x1f\x00\x00O\x80\x00'\xc0\x00\x04\xf0\x00\x08|\x04\x00\x1f\x00\x00O\x80\x00\x07\xc0\x00\x08\xf8\x000|\x04\x00\x1f\x00\x00O\x80\x00'\xc0\x00p\xff\xff\xe0\x7f\xf8\x00\x1f\xff\xff\x8f\xff\xff\xc7\xff\xff\xc0\xff\xff\xc0\x7f\xe0\x00\x1f\xff\xff\x0f\xff\xff\x87\xff\xff\x80\xff\xff\x80\x7f\xc0\x00\x1f\xff\xfc\x0f\xff\xff\x07\xff\xff\x00\xff\xfe\x00\x7f\x80\x00\x1f\xff\xf8\x0f\xff\xfc\x03\xff\xfc\x00")
speed_text = framebuf.FrameBuffer(speed_buffer, 127, 29, framebuf.MONO_HLSB)

#Raspberry pi logo lets goooo (buffer boi again defined as 'fb')
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

keypad.init()
keypad.set_brightness(1.0)

#set up the i2c protocal and initialize the displays: get addreses and set SDA/SCL pins etc.
disp1 = I2C(1,sda=Pin(26), scl=Pin(27), freq=1700000)
oled = SSD1306_I2C(128, 64, disp1)

i2c=machine.I2C(0,sda=machine.Pin(4), scl=machine.Pin(5), freq=1700000)
oled2 = SSD1306_I2C(128, 64, i2c)

def disp_big_numb(the_number): #depending on the variable that goes in it will display the correct number automatically
    oled.fill(0)
    oled2.fill(0)
    if len(str(the_number)) == 1:
        if the_number == 0:
            oled2.blit(zero_number, 0, 0)
        elif the_number == 1:
            oled2.blit(one_number, 0, 0)
        elif the_number == 2:
            oled2.blit(two_number, 0, 0)
        elif the_number == 3:
            oled2.blit(three_number, 0, 0)
        elif the_number == 4:
            oled2.blit(four_number, 0, 0)
        elif the_number == 5:
            oled2.blit(five_number, 0, 0)
        elif the_number == 6:
            oled2.blit(six_number, 0, 0)
        elif the_number == 7:
            oled2.blit(seven_number, 0, 0)
        elif the_number == 8:
            oled2.blit(eight_number, 0, 0)
        elif the_number == 9:
            oled2.blit(nine_number, 0, 0)
        
        oled2.show()
            
    elif len(str(the_number)) == 2:
        number_string = str(the_number) # change to a string so we can seperate the digits
        if number_string[0] == "1": #getting the correct number for the tenths place
            oled.blit(one_number, 91, 0)
        elif number_string[0] == "2":
            oled.blit(two_number, 91, 0)
        elif number_string[0] == "3":
            oled.blit(three_number, 91, 0)
        elif number_string[0] == "4":
            oled.blit(four_number, 91, 0)
        elif number_string[0] == "5":
            oled.blit(five_number, 91, 0)
        elif number_string[0] == "6":
            oled.blit(six_number, 91, 0)
        elif number_string[0] == "7":
            oled.blit(seven_number, 91, 0)
        elif number_string[0] == "8":
            oled.blit(eight_number, 91, 0)
        elif number_string[0] == "9":
            oled.blit(nine_number, 91, 0)
        
        
        if number_string[1] == "0": # getting the correct number for the ones place
            oled2.blit(zero_number, 0, 0)
        elif number_string[1] == "1":
            oled2.blit(one_number, 0, 0)
        elif number_string[1] == "2":
            oled2.blit(two_number, 0, 0)
        elif number_string[1] == "3":
            oled2.blit(three_number, 0, 0)
        elif number_string[1] == "4":
            oled2.blit(four_number, 0, 0)
        elif number_string[1] == "5":
            oled2.blit(five_number, 0, 0)
        elif number_string[1] == "6":
            oled2.blit(six_number, 0, 0)
        elif number_string[1] == "7":
            oled2.blit(seven_number, 0, 0)
        elif number_string[1] == "8":
            oled2.blit(eight_number, 0, 0)
        elif number_string[1] == "9":
            oled2.blit(nine_number, 0, 0)
            
        oled.show()
        oled2.show()
        
    elif len(str(the_number)) == 3:
        number_string = str(the_number) # change to a string so we can seperate the digits
        if number_string[0] == "1": #getting the correct number for the tenths place
            oled.blit(one_number, 91, 0)
        elif number_string[0] == "2":
            oled.blit(two_number, 91, 0)
        elif number_string[0] == "3":
            oled.blit(three_number, 91, 0)
        elif number_string[0] == "4":
            oled.blit(four_number, 91, 0)
        elif number_string[0] == "5":
            oled.blit(five_number, 91, 0)
        elif number_string[0] == "6":
            oled.blit(six_number, 91, 0)
        elif number_string[0] == "7":
            oled.blit(seven_number, 91, 0)
        elif number_string[0] == "8":
            oled.blit(eight_number, 91, 0)
        elif number_string[0] == "9":
            oled.blit(nine_number, 91, 0)
        
        if number_string[1] == "0": # getting the correct number for the ones place
            oled2.blit(zero_number, 0, 0)
        elif number_string[1] == "1":
            oled2.blit(one_number, 0, 0)
        elif number_string[1] == "2":
            oled2.blit(two_number, 0, 0)
        elif number_string[1] == "3":
            oled2.blit(three_number, 0, 0)
        elif number_string[1] == "4":
            oled2.blit(four_number, 0, 0)
        elif number_string[1] == "5":
            oled2.blit(five_number, 0, 0)
        elif number_string[1] == "6":
            oled2.blit(six_number, 0, 0)
        elif number_string[1] == "7":
            oled2.blit(seven_number, 0, 0)
        elif number_string[1] == "8":
            oled2.blit(eight_number, 0, 0)
        elif number_string[1] == "9":
            oled2.blit(nine_number, 0, 0)
        
        if number_string[2] == "0": # getting the correct number for the ones place
            oled2.blit(zero_number, 42, 0)
        elif number_string[2] == "1":
            oled2.blit(one_number, 42, 0)
        elif number_string[2] == "2":
            oled2.blit(two_number, 42, 0)
        elif number_string[2] == "3":
            oled2.blit(three_number, 42, 0)
        elif number_string[2] == "4":
            oled2.blit(four_number, 42, 0)
        elif number_string[2] == "5":
            oled2.blit(five_number, 42, 0)
        elif number_string[2] == "6":
            oled2.blit(six_number, 42, 0)
        elif number_string[2] == "7":
            oled2.blit(seven_number, 42, 0)
        elif number_string[2] == "8":
            oled2.blit(eight_number, 42, 0)
        elif number_string[2] == "9":
            oled2.blit(nine_number, 42, 0)
        
        oled.show()
        oled2.show()

def warp_speed(): #warp speed acrade like animation for the displays when entering the secrete mode
    oled.fill(0)
    oled.show()
    oled.blit(warp_text, 1, 17)
    oled.show()
    time.sleep(0.07)
    oled.fill(0)
    oled.blit(warp_text, 0, 14)
    oled.show()
    time.sleep(0.07)
    oled.fill(0)
    oled.blit(warp_text, 1, 16)
    oled.show()
    time.sleep(0.07)
    oled.fill(0)
    oled.blit(warp_text, 0, 14)
    oled.show()
    time.sleep(0.07)
    oled.fill(0)
    oled.blit(warp_text, 0, 15)
    oled.show()

    time.sleep(0.65)
    
    oled2.fill(0)
    oled2.show()
    oled2.blit(speed_text, 1, 16)
    oled2.show()
    time.sleep(0.07)
    oled2.fill(0)
    oled2.blit(speed_text, 0, 14)
    oled2.show()
    time.sleep(0.07)
    oled2.fill(0)
    oled2.blit(speed_text, 1, 17)
    oled2.show()
    time.sleep(0.07)
    oled2.fill(0)
    oled2.blit(speed_text, 0, 14)
    oled2.show()
    time.sleep(0.07)
    oled2.fill(0)
    oled2.blit(speed_text, 0, 15)
    oled2.show()
    
    time.sleep(0.7)

def opengate(): #two lines start the center on the bothsplays and move to the stop with smoothing then shrink out
    global close
    global up
    global down
    for i in range(0, 9):
        up = up + 2
        down = down - 2
        oled.fill(0)
        oled.hline(0, up, 128, 1)
        oled.hline(0, down, 128, 1)
        oled.show()
        oled2.fill(0)
        oled2.hline(0, up, 128, 1)
        oled2.hline(0, down, 128, 1)
        oled2.show()
    for i in range(0, 10):
        up = up + 1
        down = down - 1
        oled.fill(0)
        oled.hline(0, up, 128, 1)
        oled.hline(0, down, 128, 1)
        oled.show()
        oled2.fill(0)
        oled2.hline(0, up, 128, 1)
        oled2.hline(0, down, 128, 1)
        oled2.show()
    for i in range(0, 4):
        time.sleep(0.03)
        up = up + 1
        down = down - 1
        oled.fill(0)
        oled.hline(0, up, 128, 1)
        oled.hline(0, down, 128, 1)
        oled.show()
        oled2.fill(0)
        oled2.hline(0, up, 128, 1)
        oled2.hline(0, down, 128, 1)
        oled2.show()
    time.sleep(0.1)
    #starts closing the lines 
    for i in range(0, 48, 4):
        close = close - 8
        oled.fill(0)
        oled.hline(i, 63, close, 1)
        oled.hline(i, 0, close, 1)
        oled.show()
        oled2.fill(0)
        oled2.hline(i, 63, close, 1)
        oled2.hline(i, 0, close, 1)
        oled2.show()
    #slower closing
    for i in range(48, 64, 1):
        close = close - 2
        oled.fill(0)
        oled.hline(i, 63, close, 1)
        oled.hline(i, 0, close, 1)
        oled.show()
        oled2.fill(0)
        oled2.hline(i, 63, close, 1)
        oled2.hline(i, 0, close, 1)
        oled2.show()
        
def welcome_animation(): #its the welcome animation, in case you didnt read the title *cough*
    
    opengate()
    
    oled.fill(0)
    oled.text("|", -2, 25)
    oled.show()
    
    time.sleep(welcometext)
    oled.fill(0)
    oled.text("W|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("We|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Wel|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welc|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welco|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcom|", 0, 25)
    oled.show()
    

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcome|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()
    
def welcome_back(): #no need to explain... right?
    
    wipe_out()
    
    oled.fill(0)
    oled.text("|", -2, 25)
    oled.show()
    
    time.sleep(welcometext)
    oled.fill(0)
    oled.text("W|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("We|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Wel|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welc|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welco|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcom|", 0, 25)
    oled.show()
    

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcome|", 0, 25)
    oled.show()

    time.sleep(welcometext)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.|", 0, 25)
    oled.show()
    
    time.sleep(welcometext + 0.07)
    oled.fill(0)
    oled.text("Welcome.", 0, 25)
    oled.show()

while True:
    oled.fill(0)
    oled2.fill(0)

    turn_off = 0

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
    
    #alright where done defining stuff, put in the code!
    while True:
        keypressed = keypad.get_button_states()
        if turn_off == 1:
            break
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



    print("-= pog moment detected =-") #epic pog moment detcted when the passscode is put in correctly
    print("Awating Initialization...") #just some cool umm... i dunno sci-fi wording?
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

    up = 31
    down = 32
    close = 128
    _thread.start_new_thread(welcome_animation, ()) #starts the welcome animation on the second core

    for l in range(0,28): #fades in white background (very nice)
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

    for i in range (0, 1):  #blinks in buttons
        keypad.illuminate(0, 0, 255, 0)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(0, 55, 55, 80)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(0, 0, 255, 0)
    keypad.update()

    for i in range (0, 1): #looks cool
        keypad.illuminate(1, 30, 30, 255)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(1, 55, 55, 80)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(1, 30, 30, 255)
    keypad.update()

    for i in range (0, 1): #really adds effect
        keypad.illuminate(2, 255, 0, 255)
        keypad.update()
        time.sleep(0.1)
        keypad.illuminate(2, 55, 55, 80)
        keypad.update()
        time.sleep(0.1)
    keypad.illuminate(2, 255, 0, 255)
    keypad.update()

    for i in range (0, 1): #there are four of them
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
                    print("Entering: Whack-A-Mole") #get-em!
                    print("")
                    _thread.start_new_thread(enter_wackamole, ())
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
                                elif keypressed == 2: #1 but we dont talk about my brute forcing 
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

                                if score == 8: #set the speed depending on how far you are
                                    speed = 1.0
                                elif score == 20:
                                    speed = 0.8
                                elif score == 30:
                                    speed = 0.7
                                elif score == 45:
                                    speed = 0.6
                                elif score == 60:
                                    speed = 0.55
                                elif score == 125: #how did you- anyways its faster now
                                    speed = 0.52
                                
                                if keypressed == themole and gottem == 0:
                                    clear_board()
                                    keypad.update()
                                    gottem = 1
                                    score = score + 1
                                    disp_big_numb(score)
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
                        print("Score:", score) #oop Good Game though
                        print("---------")
                        
                        #display your failure I- I- mean succses ;)
                        oled.text("score:", 30, 20)
                        oled.show()
                        
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

                        while keypressed != 32 or keypressed != 64: #would you like to try again?
                            keypressed = keypad.get_button_states()
                            if keypressed == 64:
                                stay_in = 1
                                break
                            elif keypressed == 32:
                                stay_in = 0
                                break
                        speed = 1.5 #set the right values for the next game, good luck!
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
                    print("Entering: Matrix Man") #the matrix man wont be here for very long
                    print("")
                    button_states = keypad.get_button_states()
                    last_button_states = 0

                    wipe_out()
                    oled.text("creates a cross", 0, 25)
                    oled2.text("press a button", 0, 25)
                    oled.show()
                    oled2.show()
                    

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

                    keypad.illuminate(0, on, on, on) #epic *cough* brute forced *cough* animation
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

                    while True: #shows a cross wherever you put your very human finger
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
                                elif keypressed == 1: #0   #sets the correct column and row for the key pressed, I brute forced it... so stop reading this or maybe keep reading this jsut dont look at the code, yeah just keep reading this and wonder whereever will this lead? could there be treasure at the end? or maybe some rainbows. who knows, nobody, exepct for me, but seriusly just move on from this comment your going to be here forever I'm just listening to music while I type this so I can do this for a very long time. Please ignore spelling mistake im  not really checking. I should probably get back to coding huh. yeah I think I might. But you should keep reading this actually no just move on. here is your chance, in 1.. 2.. 3.. and go!                                                     Still here? oh, I see. You probably saw that the bar on the bottom keeps going. Well I'm actully gonna do somthing because I got an idea bai.
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
                                
                                oled.fill(0)
                                oled2.fill(0)
                                oled.text("exit: press keys", 0, 20)
                                oled.text("0 and F", 0, 32)
                                oled.show()
                                oled2.show()
                                
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
                    wipe_out()
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
                    
                    oled.text("Screen", 82, 0)
                    oled2.text("Saver", 0, 0)
                    oled.text("1980 computer", 0, 45)
                    oled2.text("RGB Lightning", 15, 45)
                    oled.show()
                    oled2.show()
                    
                    while True:
                        keypressed = keypad.get_button_states()
                        if saverleave == 1:
                            break
                        if last_button_states != keypressed:
                            if saverleave == 1:
                                break
                            last_button_states = keypressed
                            if keypressed > 0:
                                center = 15
                                saverleave = 0
                                if saverleave == 1:
                                    break
                                elif keypressed == 1:
                                    wipe_out()
                                    screen_saver_boi()
                                            
                                elif keypressed == 8:
                                    wipe_out()
                                    clear_board()
                                    time.sleep(0.5)
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
                    time.sleep(0.1)
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
                        wipe_out()
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
                        time.sleep(0.2)
                        oled2.text("== Difficulty ==", 0, 0)
                        oled2.text("Speed", 40, 25)
                        oled.text("== Difficulty ==", 0, 0)
                        oled.text("Normal", 35, 25)
                        oled.show()
                        oled2.show()
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
                                        oled.fill(0)
                                        oled2.fill(0)
                                    elif keypressed == 64:
                                        print("SPEED")
                                        SPPED = 1
                                        oled.fill(0)
                                        oled2.fill(0)
                                    elif keypressed == 256:
                                        print("=== WARP SPEED ===")
                                        Godlike = 1
                        if Godlike == 1:
                            _thread.start_new_thread(warp_speed, ())
                            time.sleep(2)
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
                        oled2.fill(0)
                        oled2.show()
                        oled.fill(0)
                        oled.text("score", 40, 10)
                        if number_of_items > 9:
                            oled.text(str(number_of_items), 55, 20)
                        else:
                            oled.text(str(number_of_items), 60, 20)
                        oled.text("key missed", 20, 35)
                        if missed_key > 9:
                            oled.text(str(missed_key), 55, 45)
                        else:
                            oled.text(str(missed_key), 60, 45)
                        oled.show()
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
                    clear_board()
                    keypad.update()
                    wipe_out()
                    time.sleep(0.1)
                    oled.text("-- Good Bye --", 7, 25)
                    oled.show()
                    time.sleep(1)
                    wipe_out()
                    turn_off = 1
                    break
                    
                if back == 1:
                    print("------------")
                    print("Welcome back")
                    print("------------")
                    _thread.start_new_thread(welcome_back, ())
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
