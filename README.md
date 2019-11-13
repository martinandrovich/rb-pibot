# rb-pibot

The objective og this project is to build a robot that can follow a wall autonomously as reliably and quickly as possible. The robot should accept start and stop commands via an ad-hoc wireless network. It should also support requests for sensor and control parameters.

This project is developed in Bash and Python, built using the CamJam EduKit 3 on a Raspberry Pi Zero, interfaced using `ssh` from a Linux console.

The Pi is assigned the IP `192.168.99.<group number>` and should be able to join the ad-hoc network `pibot`. It has a TCP server running at port `:8080`, which accepts various [commands](doc/COMMANDS.md).

## Getting started

These instructions will get you a copy of the project up and running on your Raspberry Pi for development and testing purposes, but will require the camJam EduKit 3.

### Configuration

How to connect the CamJam EduKit 3 with the Raspberry Zero.

### Dependencies

This following installations are necessary on the Pi; further dependencies are handled automatically in development environment setup via `setup.py`.

* [OpenCV 3.2](https://opencv.org/) - used for computer vision

### Installing

A guide on how to setup the Pi and port the code onto it.

### Demo

End with an example of getting some data out of the system or using it for a little demo.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/martinandrovich/rb-pro5/releases). Furthermore, this [changelog](https://github.com/martinandrovich/rb-pro5/blob/master/CHANGELOG.md) documents the most relevant changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Thanks to the supervisor [Tórur Andreassen](https://portal.findresearcher.sdu.dk/da/persons/thor-andreassen) of the LEO course at Southern University of Danmark.

