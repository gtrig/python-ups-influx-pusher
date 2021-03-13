# python-ups-influx-pusher
A python script to push ups data from nut to an influx db server

copy config.ini.example and servers.ini.example to config.ini and servers.ini to create your configuration files
the script has the ability to monitor multiple nut servers and collect data from them

#Build your image
docker build -t py-ups-parser .

#Run a new container with the generated image
docker run -it --rm py-ups-parser
