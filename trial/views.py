from django.http import  JsonResponse
import requests
import json
from rest_framework.decorators import api_view

@api_view(['POST'])
def test(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    print(received_json_data['url'])
    headers = {'content-type': 'application/json'}
    x = requests.post(received_json_data['url'], json=received_json_data['json'])
    data = x.json()
    return JsonResponse(data)
