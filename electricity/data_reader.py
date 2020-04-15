import json
from electricity.models import ElectricityData
#from django.db import models

with open('electricity/Electricityinfo.json') as f:
    data = json.load(f)

    
for result in data:
    # print(result)
    ElectricityData.objects.create(
        value=result['value'],
        variable_id = result['variable_id'],
        start_time = result['start_time'],
        end_time = result['end_time'])
           
    