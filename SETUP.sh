#!/bin/bash

echo "[+] Updating system..."
sudo apt update
sudo apt upgrade -y

echo "[+] Installing system dependencies..."
sudo apt install -y python3-pip python3-smbus i2c-tools

echo "[+] Enabling I2C..."
sudo raspi-config nonint do_i2c 0
sudo systemctl enable i2c
sudo systemctl start i2c

echo "[+] Installing Python libraries..."
python3 -m pip install luma.oled pillow psutil smbus2

echo "[+] Done!"