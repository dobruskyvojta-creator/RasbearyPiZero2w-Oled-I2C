#!/bin/bash

echo "[+] Updating system..."
sudo apt update
sudo apt upgrade -y

echo "[+] Installing Python tools..."
sudo apt install -y python3-pip python3-venv

echo "[+] Installing I2C tools..."
sudo apt install -y i2c-tools python3-smbus

echo "[+] Enabling I2C..."
sudo raspi-config nonint do_i2c 0
sudo systemctl enable i2c
sudo systemctl start i2c

echo "[+] Installing Python libraries..."
pip3 install luma.oled pillow psutil smbus2

echo "[+] Done!"
echo "Restart Raspberry Pi: sudo reboot"
echo "After reboot, run: i2cdetect -y 1"