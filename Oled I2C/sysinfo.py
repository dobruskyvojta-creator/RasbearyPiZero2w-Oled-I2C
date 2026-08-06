# In this code we will get the system information of the Raspberry Pi and display it on the OLED screen using I2C communication.

#Imports
import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

i2c = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
    
# TEMP watch -n 1 vcgencmd measure_temp
# what we want : TEMP CPU ... TEMP OUTSIDE ... CLOCK + DATE .. BATTER and IP 