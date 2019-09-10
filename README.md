# i3-battery-alert

Python script to notify on battery low level with playing audio

Python Version: `3.7`


## How to use

```
# first install required modules
pip3 install -r requirements.txt

# then run the script
python3 i3-battery-alert.py

# OR run the script from i3 config file on startup by adding this command to the config file
exec --no-startup-id i3-battery-alert.py

# don't forget to make the script executable
chmod u+x i3-battery-alert.py
```

NOTE: If you are going to add the script in i3 config file then don't forget to add the script dir into the __PATH__ env var

`export PATH=$PATH:{path/to/script/dir}`

> NOTE: add the above line into your __.bashrc__ or __.zshrc__ [if you are using Z shell]
