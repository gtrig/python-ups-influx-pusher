# Description
python-ups-influx-pusher is a python script to push ups data from nut to an influx db server


# Installation

## Generate configuration files
copy config.ini.example and servers.ini.example to config.ini and servers.ini to create your configuration files
the script has the ability to monitor multiple nut servers and collect data from them
```
cp config.ini.example config.ini
cp servers.ini.example servers.ini
```

## Build your image
```
docker build -t py-ups-parser .
```

## Run a new container with the generated image
```
docker run -it --rm py-ups-parser
```