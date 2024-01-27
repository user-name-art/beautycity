
# from django.http import JsonResponse
from django.http import JsonResponse
from beautycityapp.models import Studio, Service, Master, MastersService


def get_masters(request):
    if request.method == 'POST':
        response = dict(request.POST)
        studio_id = response['studio_id'][0]
        service_id = response['service_id'][0]
        studio = Studio.objects.get(id=studio_id)
        masters = Master.objects.filter(studio=studio)
        service = Service.objects.get(id=service_id)
        master_services = MastersService.objects.filter(service=service)
        
        # print(masters)
        studio_masters={}
        for master in master_services:
            studio_masters[master.master.id] = {
                'id': master.master.id,
                'name': master.master.name,
                'prof': master.master.profession,
                'photo_url': master.master.photo.url
            }
        return JsonResponse(studio_masters) 

