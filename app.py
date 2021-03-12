from nut import nutPullData
from datetime import datetime
import time
import configparser

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

server_config = configparser.ConfigParser()
server_config.read("./nut_servers.ini")
general_config = configparser.ConfigParser()
general_config.read("./config.ini")

#Influx configuration loading
influx_url = general_config.get('influx','url')
token = general_config.get('influx','token')
org = general_config.get('influx','org')
bucket = general_config.get('influx','bucket')

client = InfluxDBClient(url=influx_url, token=token)

while True:
    ups_data = []
    for server in server_config.sections():
        ups_data.append(nutPullData(host=server_config.get(server,'host'),port=server_config.get(server,'port'),username=server_config.get(server,'username'),password=server_config.get(server,'password')))
        
        
    power_ok=True
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for ups in ups_data:
        if ups == False: 
            continue
        if ups['ups.status']!='OL' or ups['battery.charge']<100 :
            power_ok=False
        
        point = Point("ups")
        point.tag("ups_name", ups['name'] )    
        for entry in ups:
            if isinstance(ups[entry],(float,int)):
                point.field(entry, ups[entry])
        
        point.time(datetime.utcnow(), WritePrecision.NS)
        try:
            write_api.write(bucket, org, point)
            print('data sent')
        except:
            print('Couldnt send data to influx')
    
    if power_ok:
        time.sleep(general_config.getint('timing','OK_INTERVAL'))
    else:
        time.sleep(general_config.getint('timing','NOT_OK_INTERVAL'))