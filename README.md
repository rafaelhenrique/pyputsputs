# pyputsputs
Show sound wave on Arduino leds using Pingo.io

## What this project do?

See video: https://www.youtube.com/watch?v=MbYySNSVVFo

Capture sound waves with microphone of computer and then represent this wave on leds of arduino using Pingo.io.

## What do you need?
The hardware used is an Arduino Uno and the components are:
- 6 120 Ω resistors;
- 6 3mm LEDs;
- Some jumpers;
- Some noise.

## How i install/use this project?
When you use pingo/pyfirmata we need preload StandardFirmata on your board, on ARDUINO IDE preload this example on menus:

```"File" -> "Examples" -> "Firmata" -> "StandartFirmata"```


## Arduino Setup

![Arduino](https://raw.githubusercontent.com/akarokr/pyputsputs/master/contrib/draw.png "Arduino")

## Clone the project

```
$ git clone git@github.com:rafaelhenrique/pingo_experiments.git
```

Create an virtualenv (I like the [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenv-wrapper")):

```
$ mkvirtualenv -p /usr/bin/python2.7 pyputsputs
```

Enter on pingo-io directory and installs pingo ([recommended by developers](http://www.pingo.io/docs/#installing-from-github)). 


```
$ cd pingo-io
$ python setup.py develop
```

Install requirements:

```
$ pip install -r requirements.txt
```

Connect your arduino into usb port and then run:

```
$ python run.py

```
## Possible Problems

**StandardFirmata don't work**

If you're having some problems with the StandardFirmata, add the SoftwareSerial header with the code inclues:

```
#include <SoftwareSerial.h>
```

**pingo-io is empty**

If the pingo-io is an empty directory, clone the ([project](https://github.com/pingo-io/pingo-py/tree/091192f0381cd107685b55a258024be8c88e38cc)) and then run the following commands:
```
$ cd pingo-io
$ python setup.py develop
```
