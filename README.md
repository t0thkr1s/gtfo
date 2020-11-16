# gtfo

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/t0thkr1s/)

This is a standalone script written in Python 3 for [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io).
You can search for Unix binaries that can be exploited to bypass system security restrictions.
These binaries can be abused to ~~get the f**k~~ break out of restricted shells, escalate privileges, transfer files, spawn bind and reverse shells, etc...

The functions are from [https://github.com/GTFOBins/GTFOBins.github.io](https://github.com/GTFOBins/GTFOBins.github.io) and all credit goes to its respective contributors.
They are simplified (no need for environmental variables) and syntax highlighted.

## Download

```
git clone https://github.com/t0thkr1s/gtfo
```

## Install

The script has 2 dependencies:

*   [colorama](https://pypi.org/project/colorama/)
*   [pygments](https://pypi.org/project/Pygments/)

You can install these by typing:

```
python3 setup.py install
```

## Run

```
python3 gtfo.py [binary]
```

## Screenshots


Screenshot 1             |  Screenshot 2
:-----------------------:|:-----------------------:
![Screenshot1](https://i.imgur.com/1EzFiGQ.png)  |  ![Screenshot2](https://i.imgur.com/icgmDct.png)


### Disclaimer

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
