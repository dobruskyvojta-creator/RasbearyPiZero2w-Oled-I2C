# In this code we will get the system information of the Raspberry Pi and display it on the OLED screen using I2C communication.

#Imports Libraries

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil
import smbus2
import subprocess
import board
import busio

#Imports
from oled_i2c.cpu_temp import draw_cpu_temp

#comunication with the OLED display trought pins
i2c = busio.I2C(board.SCL, board.SDA)

#The size of the display
WIDTH = 128 
HEIGHT = 64

#Display 
oled = adafruit_ssd1306.SSD1306_I2C(
    WIDTH,
    HEIGHT,
    i2c,
)


# Clear the display
oled.fill(0)
oled.show()

# Create a blank image for drawing.
image = Image.new(
    "1",
    (WIDTH, HEIGHT)
)

# Get a drawing object to draw on the image.
draw = ImageDraw.Draw(image)


draw_cpu_temp(draw)

oled.image(image)
oled.show()
# what we want : 1. TEMP CPU ... .2 BATTERY % ... CLOCK + DATE  and IP & TEMP OUTSIDE