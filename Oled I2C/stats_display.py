# In this code we will get the system information of the Raspberry Pi and display it on the OLED screen using I2C communication.

#Imports
from curses import raw

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil
import smbus2
import subprocess
import board
import busio

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
    addr=0x3C
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

# Draw the CPU temperature on the OLED display
draw.text(
    (0, 0),
    "TEMP CPU: {} C".format(psutil.sensors_temperatures()['cpu_thermal'][0].current),
    font=ImageFont.load_default(),
    fill=255
)


def cpu_temp(draw):
    draw.text(
        (30, 40),
        "TEMP CPU: {} C".format(psutil.sensors_temperatures()['cpu_thermal'][0].current),
        font=ImageFont.load_default(),
        fill=255
)

cpu_temp(draw)

oled.image(image)
oled.show()
# what we want : TEMP CPU ... TEMP OUTSIDE ... CLOCK + DATE .. BATTERY and IP 