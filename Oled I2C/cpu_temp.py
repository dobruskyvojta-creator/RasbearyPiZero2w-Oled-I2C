

# Draw the CPU temperature on the OLED display
def draw_cpu_temp(draw):
    draw.text(
        (0, 0),
        "TEMP CPU: {} C".format(psutil.sensors_temperatures()['cpu_thermal'][0].current),
        font=ImageFont.load_default(),
        fill=255
)
