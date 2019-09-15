# i3-battery-alert

Python script to notify on battery low level with playing audio

Python Version: `3.7`


## Download and use the script

```bash
# clone the repo
git clone https://github.com/Davenchy/i3-battery-alert.git
cd i3-battery-alert

# install required modules
pip3 install -r requirements.txt

# try to run the script
python3 i3-battery-alert.py
```

## Auto Install

- Add the script to systemd from [here](#to-run-the-script-on-system-boot)

OR

- Install the script by the __install.sh__ shell script

```bash
# make the install and uninstall scripts executable
chmod u+x install.sh
chmod u+x uninstall.sh

# to install
./install.sh

# to uninstall
./uninstall.sh
```


## To make the script executable

```bash
chmod u+x i3-battery-alert.py
sudo ln -s `pwd`/i3-battery-alert.py /usr/bin/i3-battery-alert

# now try to run
i3-battery-alert
```

## To run the script on system boot

> Using systemd

> Note: You need to make the script [executable](#to-make-the-script-executble) first

```bash
# copy the service file
sudo cp i3-battery-alert.service /usr/lib/systemd/system

# start the service
sudo systemctl start i3-battery-alert

# to enable the script to run on system boot
sudo systemctl enable i3-battery-alert
```

for systemd more information from [here](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)