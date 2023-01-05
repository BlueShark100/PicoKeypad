import picokeypad as keypad
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

last_button_states = 0

keypad.init()

out = 0

i2c=machine.I2C(0,sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
oled2 = SSD1306_I2C(128, 64, i2c)

disp1 = I2C(1,sda=Pin(26), scl=Pin(27), freq=400000)
oled = SSD1306_I2C(128, 64, disp1)


out = 0
last_button_states = 0

while True:
    keypressed = keypad.get_button_states()
    if out == 1:
        break
    if last_button_states != keypressed:
        last_button_states = keypressed
        if keypressed > 0:
            print(keypressed)
            out = 1

oled.fill(0)
oled.text("FRIC", 0, 25)
oled.show()

time.sleep(0.2)

out = 0
last_button_states = 0

while True:
    keypressed = keypad.get_button_states()
    if out == 1:
        break
    if last_button_states != keypressed:
        last_button_states = keypressed
        if keypressed > 0:
            print(keypressed)
            out = 1
            
oled2.fill(0)
oled2.text("YES", 0, 25)
oled2.show()