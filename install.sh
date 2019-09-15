#!/bin/bash

# make the script executable
chmod u+x i3-battery-alert.py
sudo ln -s `pwd`/i3-battery-alert.py /usr/bin/i3-battery-alert

# add service to systemd
sudo cp i3-battery-alert.service /usr/lib/systemd/system
sudo systemctl start i3-battery-alert
sudo systemctl enable i3-battery-alert