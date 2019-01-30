from django.http import JsonResponse
from django.views import View
from .models import Hero
import json

class Heroes(View):
    def get(self, req):
        heroes= list(Hero.objects.values().all())
        return JsonResponse({'status': 'OK', 'heroes': heroes})
    
    def post(self, req):
        # without decode() what we get back in the print is a bite value, decode() get the data and turn it in to the utf8 type
        # print(req.body) return bite type of data
        # print( req.body.decode())
        #buttom line takes the utf8 type and turn in to json with the import json at the top
        body = json.loads(req.body.decode())
        print(body)
        Hero.objects.create(
            alias= body['alias'],
            secret =body['secret'],
            desc =body['desc']
        )
        # print(body, type(body))
        return JsonResponse({'status': 'OK', 'message': "post"})
    

