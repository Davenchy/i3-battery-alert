#!/bin/bash

# make the script not executable
sudo rm /usr/bin/i3-battery-alert

# remove service from systemd
sudo systemctl stop i3-battery-alert
sudo systemctl disable i3-battery-alert
sudo rm /usr/lib/systemd/system/i3-battery-alert.service