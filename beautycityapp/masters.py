
# from django.http import JsonResponse
from django.http import JsonResponse
from beautycityapp.models import Studio, Service, Master
from django.shortcuts import render

def get_masters(request):
    if request.method == 'POST':
        response = dict(request.POST)
        studio_id = response['studio_id'][0]
        service_id = response['service_id'][0]
        studio = Studio.objects.get(id=studio_id)
        service = Service.objects.get(id=service_id)
        masters = Master.objects.filter(studio=studio, services=service)
        # print(masters)
        studio_masters={}
        for master in masters:
            print(master)
            # dict.setdefault(key[, default])
            studio_masters[master.id] = {
                'name': master.name,
                'prof': 'aaa'
            }
        return JsonResponse(studio_masters) 

