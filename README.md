# pykush
```
  __   __         _    _ _
  \ \ / /__ _ __ | | _(_) |_
   \ V / _ \ '_ \| |/ / | __|
    | |  __/ |_) |   <| | |_
    |_|\___| .__/|_|\_\_|\__|
           |_|
```
**[Yepkit](http://www.yepkit.com/) [YKUSH](https://www.yepkit.com/products/ykush) Python library and command line tool**

Provides library and command line functionality for communicating with a [YKUSH](https://www.yepkit.com/products/ykush) device over USB.

Thanks to the developers and maintainers of the following projects among others:
- [HIDAPI](https://github.com/signal11/hidapi) multi-platform library
- Python [hidapi](https://pypi.python.org/pypi/hidapi) wrapper module
- Python [hidapi-cffi](https://pypi.python.org/pypi/hidapi-cffi) wrapper module
Any of the above python wrappers are currently supported.

## Features

- Easy to [use](https://github.com/Yepkit/pykush#usage)
- Written to support [YKUSH]((https://www.yepkit.com/products/ykush)), the Yepkit USB Switchable Hub
- Open-source, please be our guest to collaborate
- Current development version supports both Python 2 and 3
- Works on Linux, Windows and Mac

## Requirements

- A Linux, Windows or Mac (OS X) system
- A [YKUSH](https://www.yepkit.com/products/ykush) device
- A recent [Python 2 >=2.7.9 or Python 3 >=3.4](https://www.python.org/downloads/) installed
- [hidapi](https://pypi.python.org/pypi/hidapi) or [hidapi-cffi](https://pypi.python.org/pypi/hidapi-cffi) module installed

## Installation

If you are in a hurry and just need a console application you can give our Pyinstaller bundled executable a try:
- [Windows](https://github.com/Yepkit/pykush/releases/download/v0.3.6/windows.zip) executable, Windows XP or newer
- [macOS](https://github.com/Yepkit/pykush/releases/download/v0.3.6/macos.zip) executable, El Capitan or newer
- [Linux x86_64](https://github.com/Yepkit/pykush/releases/download/v0.3.6/linux64.zip), kernel 2.6 or newer
- [Linux i386](https://github.com/Yepkit/pykush/releases/download/v0.3.6/linux32.zip), kernel 2.6 or newer

Download the executable corresponding to your platform and run it from a terminal window.
Also remember to authorize execution on Linux or macOS systems:
```bash
$ chown u+x pykush
$ ./pykush -l
```

### From source

Anonymous:
```bash
$ git clone https://github.com/Yepkit/pykush
$ cd pykush/
$ python setup.py install
```

Git:
```bash
$ git clone git@github.com:Yepkit/pykush
$ cd pykush/
$ python setup.py install
```

### With python pip

```bash
$ pip install yepkit-pykush
```

## Usage

### Basic command line usage

```bash
$ python pykush.py -h
usage: pykush.py [-h] [-s SERIAL]
                 (-l | -u [UP [UP ...]] | -d [DOWN [DOWN ...]] | -r READ | -w WRITE WRITE | -p)

Yepkit YKUSH command line tool.

optional arguments:
  -h, --help            show this help message and exit
  -s SERIAL, --serial SERIAL
                        specify the serial number string of the YKUSH to be
                        listed or managed
  -l, --list            list YKUSH devices
  -u [UP [UP ...]], --up [UP [UP ...]]
                        the downstream port numbers to power up, none means
                        all
  -d [DOWN [DOWN ...]], --down [DOWN [DOWN ...]]
                        the downstream port numbers to power down, none means
                        all
  -r READ, --read READ  the GPIO pin to read from
  -w WRITE WRITE, --write WRITE WRITE
                        the GPIO pin to write to
  -p, --persist         make the current running configuration persistent
                        across reboots (only supported on devices with
                        firmware v2.0 and above)

$ python pykush.py -l
listing YKUSH family devices
  found a YKUSH release 2 device with serial number YK20001
    system device path 0001:000a:00, vendor id 0x04d8, product id 0xf2f7
    the device is running a v1.2 firmware and has 3 downstream ports
    downstream running power states, port 1 to 3: UP, UP, UP

$ python pykush.py -d 1 2
managing YKUSH family devices
  found a YKUSH release 2 device with serial number YK20001
    system device path 0001:000a:00, vendor id 0x04d8, product id 0xf2f7
    the device is running a v1.2 firmware and has 3 downstream ports
    powering DOWN port 1... done
    powering DOWN port 2... done
```

### Basic module programming usage
```bash
$ python
>>> import pykush.pykush as pykush
>>> yk = pykush.YKUSH()
>>> yk.set_allports_state_up()
True
>>> yk.get_downstream_port_count()
3
>>> yk.set_port_state(2, pykush.YKUSH_PORT_STATE_DOWN)
True
>>> yk.get_port_state(2)
0
>>> yk.get_port_state(2) == pykush.YKUSH_PORT_STATE_DOWN
True
>>>
```

## Disclaimer

The module is already usable in the limited scope we tested but it is still in a alpha stage.

## Contributing

### Bug Reports

If you find a problem, please submit a bug report on [issue tracker](https://github.com/Yepkit/pykush/issues).
