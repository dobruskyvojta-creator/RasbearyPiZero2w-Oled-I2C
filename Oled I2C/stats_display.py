# In this code we will get the system information of the Raspberry Pi and display it on the OLED screen using I2C communication.

#Imports
import luma.oled
import Pillow
import psutil
import smbus2

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0


    
# TEMP watch -n 1 vcgencmd measure_temp
# what we want : TEMP CPU ... TEMP OUTSIDE ... CLOCK + DATE .. BATTER and IP 