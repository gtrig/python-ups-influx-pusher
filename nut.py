from nut2 import PyNUTClient
import json
import numbers

def nutPullData(host, port, username, password):
    try:
        nut = PyNUTClient(host=host,port=port,login=username,password=password)
    except:
        print("there was an error connecting to host:"+host)
        return False

    for ups_name, ups_description in nut.list_ups().items():
        ups_vars = nut.list_vars(ups_name)
        ups_vars['name'] = ups_name
        if ups_vars['device.type'] != 'ups':
            continue

        for element in ups_vars:
            if ups_vars[element].replace('.','',1).isdigit():
                ups_vars[element] = float(ups_vars[element])
    
    return ups_vars