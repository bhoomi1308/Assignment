from django.apps import AppConfig
import json
from django.http import StreamingHttpResponse


class Assignment(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

json_data = open(r'Desktop/sample.json')   
data1 = json.load(json_data) # deserialises it
data2 = json.dumps(data1) # json formatted string
json_data.close()
def main_page(request):
    if request.method=='POST':
            received_json_data=json.loads(request.body)
            return StreamingHttpResponse('it was post request: '+str(received_json_data))
    return StreamingHttpResponse('it was GET request')
