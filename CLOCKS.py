#ONLY THING MADE BY AI IN THIS PROJECT ONLY A FUN THING AS A BONUS 
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import board
import busio
import time
import datetime
import random

# OLED
i2c = busio.I2C(board.SCL, board.SDA)
WIDTH = 128
HEIGHT = 64

oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Načtení fontů (čas má teď zvětšenou velikost na 26)
try:
    font_date = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    font_time = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
except:
    font_date = ImageFont.load_default()
    font_time = ImageFont.load_default()

# Bublinky po stranách (mimo střed, kde je text)
bubbles = []
for _ in range(14):
    if random.choice([True, False]):
        x = random.randint(2, 22)    # Levý sloupec
    else:
        x = random.randint(106, 126) # Pravý sloupec
    y = random.randint(0, HEIGHT)
    speed = random.uniform(0.4, 1.2)
    radius = random.choice([1, 2])
    bubbles.append({"x": x, "y": y, "speed": speed, "radius": radius})

def get_text_size(draw, text, font):
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
    else:
        return draw.textsize(text, font=font)

# Hlavní smyčka hodin
while True:
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    # 1. Bublinky
    for b in bubbles:
        b["y"] -= b["speed"]
        if b["y"] < -5:
            b["y"] = HEIGHT + 5
            if random.choice([True, False]):
                b["x"] = random.randint(2, 22)
            else:
                b["x"] = random.randint(106, 126)
        
        if b["radius"] == 1:
            draw.point((int(b["x"]), int(b["y"])), fill=255)
        else:
            r = b["radius"]
            bx, by = int(b["x"]), int(b["y"])
            draw.ellipse([bx - r, by - r, bx + r, by + r], outline=255, fill=0)

    # 2. Čas a datum
    now = datetime.datetime.now()
    date_str = now.strftime("%d. %m. %Y")
    time_str = now.strftime("%H:%M:%S")

    # 3. Pozice textu
    date_w, date_h = get_text_size(draw, date_str, font_date)
    time_w, time_h = get_text_size(draw, time_str, font_time)

    date_x = (WIDTH - date_w) // 2
    date_y = 4   # Malé datum nahoře

    time_x = (WIDTH - time_w) // 2
    time_y = 22  # Velký čas (posunutý níš, aby nezabíral místo nahoře)

    # 4. Kreslení
    draw.text((date_x, date_y), date_str, font=font_date, fill=255)
    draw.text((time_x, time_y), time_str, font=font_time, fill=255)

    # 5. Zobrazení
    oled.image(image)
    oled.show()

    time.sleep(0.03)