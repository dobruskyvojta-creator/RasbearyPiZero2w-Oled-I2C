from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import board
import busio
import time
import BACKEND






# OLED
i2c = busio.I2C(board.SCL, board.SDA)
WIDTH = 128
HEIGHT = 64

oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)


# Hlavní smyčka
while True:
    CPU_TEMP, CPU_USAGE, P, IP, TOTAL_MEM_SPACE, MEM_AVAILABLE = BACKEND.get_system_stats()

    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    # draw.text((0, 0), "RASPBERRY PI ZERO 2 WH", fill=255)
    # draw.text((0, 9), f"IP ADRESS: {IP}%", fill=255)
    # draw.text((0, 18), f"CPU TEMP: {CPU_TEMP}%", fill=255)
    # draw.text((0, 27), f"CPU USAGE: {CPU_USAGE}%", fill=255)
    # draw.text((0, 35), f"TOTAL_MEM_SPACE: {TOTAL_MEM_SPACE}%", fill=255)
    # draw.text((0, 45), f"MEM_AVAILABLE: {MEM_AVAILABLE}%", fill=255)
    # draw.text((0, 54), f"BATTERY: {P:.1f}%", fill=255)

    draw.text((0, 0), "PI ZERO 2 W", fill=255)
    draw.text((0, 10), f"IP: {IP}", fill=255)

    draw.text((0, 22), f"CPU: {CPU_TEMP}C", fill=255)
    draw.text((68, 22), f"LOAD: {CPU_USAGE}%", fill=255)

    draw.text((0, 34), f"RAM: {TOTAL_MEM_SPACE}", fill=255)
    draw.text((68, 34), f"FREE: {MEM_AVAILABLE}", fill=255)

    draw.text((0, 50), f"BATTERY: {P:.1f}%", fill=255)
    

    
    oled.image(image)
    oled.show()

    time.sleep(2)
    