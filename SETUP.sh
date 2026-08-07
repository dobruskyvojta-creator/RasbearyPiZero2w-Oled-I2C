#!/bin/bash

echo "[+] Updating system..."
sudo apt update
sudo apt upgrade -y


echo "[+] Installing system dependencies..."
sudo apt install -y \
python3-pip \
python3-smbus \
i2c-tools \
python3-pil


echo "[+] Enabling I2C..."
sudo raspi-config nonint do_i2c 0


echo "[+] Installing Python libraries..."
python3 -m pip install --break-system-packages \
adafruit-circuitpython-ssd1306 \
pillow \
psutil \
smbus2


echo "[+] Testing libraries..."

python3 - <<EOF
import adafruit_ssd1306
import PIL
import psutil
import smbus2

print("Libraries OK")
EOF


echo "[+] Done!"

echo "[!] Please reboot your Raspberry Pi to apply changes.[!]"