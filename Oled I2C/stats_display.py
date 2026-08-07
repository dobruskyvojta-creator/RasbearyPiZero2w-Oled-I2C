# In this code we will get the system information of the Raspberry Pi and display it on the OLED screen using I2C communication.

#Imports
from PIL import Image, ImageDraw
import luma.oled
import psutil
import smbus2

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

from PIL import Image, ImageDraw

image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

draw.line((0, 10, 127, 10), fill=255)

image.show()
    
# TEMP watch -n 1 vcgencmd measure_temp
# what we want : TEMP CPU ... TEMP OUTSIDE ... CLOCK + DATE .. BATTER and IP 