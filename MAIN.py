from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import psutil
import board
import busio
import time

# Tvoje vlastní draw funkce
from oled_i2c.cpu_temp import draw_cpu_temp

# INA219
from ina219 import INA219
ina = INA219(addr=0x43)          # ← zkontroluj adresu (i2cdetect -y 1)

# OLED
i2c = busio.I2C(board.SCL, board.SDA)
WIDTH = 128
HEIGHT = 64
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Font
font = ImageFont.load_default()

def draw_battery(draw, ina):
    percent = ina.getPercent()
    draw.text((0, 16), f"BATERIE: {percent} %", font=font, fill=255)

# Hlavní smyčka
while True:
    # Vytvoř čistý obrázek
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    # Nakresli, co chceš
    draw_cpu_temp(draw)          # TEMP CPU
    draw_battery(draw, ina)      # BATERIE %

    # Sem později přidáš:
    # draw_clock(draw)
    # draw_ip(draw)
    # draw_outside_temp(draw)

    # Zobraz
    oled.image(image)
    oled.show()

    time.sleep(2)