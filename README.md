# RaspberrySenseWeatherStation
A Web Application based on Python which shows weather data.

# Installation
First you need to have a RaspberryPi, a Sense HAT and an up-to-date version of Raspbian.

Then install the Sense HAT software package:

```
sudo apt-get install sense-hat
sudo pip3 install pillow
```

Then reboot your pi:

```
sudo reboot
```

When you've done that, you need to install Flask, the framework we are going to be using for our Python-powered web server:

```
sudo apt-get install python3-flask
```

# Usage

To run the application, just clone the repository, cd into it and run with Python3:

```
cd RaspberrySenseWeatherStation/
python3 app.py
```

Note that temperature and humidity readings can be offset by a few degrees and/or percents. This is because the CPU temperature influences the temperature sensor on the Sense HAT, especially on the RaspberryPi 3. By default it is corrected by substracting the reading by a certain value based on the CPU temperature. You can change this value in weatherstation.py based on your specific setup and workload.
