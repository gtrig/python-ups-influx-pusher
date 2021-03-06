#! /usr/bin/env python3

from nut2 import PyNUTClient
import json
import numbers

def nutPullData(host, port, username, password):
    nut = PyNUTClient(host=host,port=port,login=username,password=password)

    for ups_name, ups_description in nut.list_ups().items():
        ups_vars = nut.list_vars(ups_name)
        ups_vars['name'] = ups_name
        if ups_vars['device.type'] != 'ups':
            continue

        for element in ups_vars:
            if ups_vars[element].replace('.','',1).isdigit() :
                ups_vars[element] = float(ups_vars[element])
                #print(ups_vars[element])
        
        #data = json.loads(json.dumps(ups_vars))
        
        # json_data = {'data':{
        #     'measurement': 'ups',
        #     'tags': {
        #         'name': ups_name,
        #         'description': ups_description,
        #         'status': ups_vars['ups.status'],
        #     },
        #     'fields': data
        # }}
    
    return ups_vars


#     # influxdb_client.write_points([{
#     #     'measurement': 'ups',
#     #     'tags': {
#     #         'name': ups_name,
#     #         'description': ups_description,
#     #         'battery_type': ups_vars['battery.type'],
#     #         'manufacturer': ups_vars['device.mfr'],
#     #         'model': ups_vars['device.model'],
#     #         'status': ups_vars['ups.status'],
#     #     },
#     #     'fields': {
#     #         'battery_charge': float(ups_vars['battery.charge']),
#     #         'battery_charge_low': float(ups_vars['battery.charge.low']),
#     #         'battery_runtime': float(ups_vars['battery.runtime']),
#     #         'input_frequency': float(ups_vars['input.frequency']),
#     #         'input_transfer_high': float(ups_vars['input.transfer.high']),
#     #         'input_transfer_low': float(ups_vars['input.transfer.low']),
#     #         'input_voltage': float(ups_vars['input.voltage']),
#     #         'output_frequency': float(ups_vars['output.frequency']),
#     #         'output_frequency_nominal': float(ups_vars['output.frequency.nominal']),
#     #         'output_voltage': float(ups_vars['output.voltage']),
#     #         'output_voltage_nominal': float(ups_vars['output.voltage.nominal']),
#     #         'delay_shutdown': float(ups_vars['ups.delay.shutdown']),
#     #         'delay_start': float(ups_vars['ups.delay.start']),
#     #         'load': float(ups_vars['ups.load']),
#     #         'power': float(ups_vars['ups.power']),
#     #         'power_nominal': float(ups_vars['ups.power.nominal']),
#     #         'power_real': float(ups_vars['ups.realpower']),
#     #         'timer_shutdown': float(ups_vars['ups.timer.shutdown']),
#     #         'timer_start': float(ups_vars['ups.timer.start']),
#     #     },
#     # }])
