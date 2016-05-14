# pyputsputs
Show sound wave on Arduino leds using Pingo.io

## What this project do?

See video: https://www.youtube.com/watch?v=MbYySNSVVFo

Capture sound waves with microphone of computer and then represent this wave on leds of arduino using Pingo.io.

## How i install/use this project?

When you use pingo/pyfirmata we need preload StandardFirmata on your board, on ARDUINO IDE preload this example on menus:

```"File" -> "Examples" -> "Firmata" -> "StandartFirmata"```

We need connect cables and leds on your Arduino :

![Arduino](/contrib/draw.png "Arduino")

Clone this project:

```
$ git clone git@github.com:rafaelhenrique/pingo_experiments.git
```

Create an virtualenv (i prefer [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenv-wrapper")):

```
$ mkvirtualenv pyputsputs
```

Enter on pingo-io directory and installs pingo ([recommended by developers](http://www.pingo.io/docs/#installing-from-github)):

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
