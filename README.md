# Arduino iOT project
![alt text](https://github.com/abhineetraj1/arduino-iot-project/blob/main/fav.png?raw=true)

* RGB led blinking through website hosted under home network.
* User can controll the blinking of RGB light through web portal  from any device connected under same network
* Python + Arduino project.

## Requirements
* Arduino board
* RGB light
* Buzzer
* Battery

## Installation
1) Download Arduino IDE from [here](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE)
2) Download this repo
3) Upload ```StandardFirmata.ino``` code in arduino
4) Download python3.X and install libraries in ```requirements.txt``` through this command:-
```
pip3 install -r requirements.txt
```


## Circuit of Arduino

| Arduino PINs | Electronic device |
|------|:------:|
|  Pin 2 | Positive terminal of buzzer |
|  Pin 3 | Red terminal of rgb light |
|  Pin 4 | Green terminal of rgb light |
|  Pin 5 | Blue terminal of rgb light |
|  GND   | Negative terminal of buzzer |
|  5V    | Cathode point of RGB light |

## Execution
1)	Connect arduino with your system
2)	Open file ```StandardFirmata.ino``` and upload the folder
3)	Download this repo
```
git clone https://github.com/abhineetraj1/arduino-iot-project
```
4)	Open the folder of code
```
cd arduino-iot-project
```
5)	Open terminal in that folder
6)	Enter folder code into terminal and hit enter
```
flask run -h 0.0.0.0
```
7)	Open any device that is connected to same network or wifi
8)	Open the url (printed in the terminal)

Enjoy!!

### Note:-	
Make sure you have connected the laptop and the mobile with same network or wifi

## Uses
*	This can be used as an application in smart home system, where your can turn on and off appliances according to your will thorugh your mobile phone or devices connected under home network.
*	This can be used in smart office, where your can turn on and off office lights, systems ...etc according to your will thorugh your mobile phone or devices connected under home network.
*	This can be used as an application in smart class, where your can turn on and off hall lights according to your will thorugh your mobile phone or devices connected under home network.

## Programming languages used
<a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.arduino.cc/header-footer/prod/assets/favicon-arduino/favicon.ico" alt="blender" width="40" height="40"/> </a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>

## Developer
*	[abhineetraj1](http://github.com/abhineetraj1)
