# rb-pibot

The objective og this project is to build a robot that can follow a wall autonomously as reliably and quickly as possible. The robot should accept start and stop commands via an ad-hoc wireless network. It should also support requests for sensor and control parameters.

![CamJam EduKit 3 - Robotics](http://camjam.me/wp-content/uploads/2015/09/Edukit3_1500-Alex-Eames-sm.jpg)

This project is developed in Bash and Python, built using the CamJam EduKit 3 on a Raspberry Pi Zero, interfaced using `ssh` from a Linux console.

The Pi is assigned the IP `192.168.99.<group number>` and should be able to join the ad-hoc network `pibot`. It has a TCP server running at port `:8080`, which accepts various [commands](doc/COMMANDS.md).

## Getting started

These instructions will get you a copy of the project up and running on your Raspberry Pi with the camJam EduKit 3 for development and testing purposes.

The controller is running on Rasbian Stretch Lite (2019-04-08) with Python 3.5 (installed per default). The robot is assembled as instructed by the EduKit guide, with the ultrasound sensor being mounted on and pointing towards the left side.

The only external dependency is the `rpi.GPIO` package for Python 3, which can be installed via the command:

```bash
sudo apt install python3-rpi.gpio
```

Once downloaded, the python module can be run from the root directory of the project using:

```bash
python3 -m pibot
```

Commands can be issued to the Pi using `socat` via the terminal, with the IP address and port by defualt set to `localhost:8080` (can be configured in `app.py`). The robot can be started by using the command:

```bash
printf start | socat - tcp:localhost:8080
```

In order to communicate with the robot wirelessly, SSH must be enabled on the Raspberry Pi. It is then possible to configure the Pi to connect to an ad-hoc network or simply communicate with it using SSH over the WiFi. The IP address of the Pi's server must be configured accordingly.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/martinandrovich/rb-pro5/releases). Furthermore, this [changelog](https://github.com/martinandrovich/rb-pro5/blob/master/CHANGELOG.md) documents the most relevant changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Thanks to the supervisor [Tórur Andreassen](https://portal.findresearcher.sdu.dk/da/persons/thor-andreassen) of the LEO course at Southern University of Danmark.

