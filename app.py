from nut import nutPullData
from datetime import datetime
import time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "influxtoken"
org = "none"
bucket = "ups_data"

client = InfluxDBClient(url="http://192.168.8.200:8086", token=token)

while True:
    ups_data = [
        nutPullData(host='192.168.8.200',port='3493',username='monuser',password='pass'),
        nutPullData(host='192.168.8.180',port='3493',username='monuser',password='pass')
    ]
        
    power_ok=True
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for ups in ups_data:
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
        time.sleep(30)
    else:
        time.sleep(1)