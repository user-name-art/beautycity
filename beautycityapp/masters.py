
# from django.http import JsonResponse
from django.http import JsonResponse
from beautycityapp.models import Studio, Service, Master, Profession


def get_masters(request):
    if request.method == 'POST':
        response = dict(request.POST)
        studio_id = response['studio_id'][0]
        service_id = response['service_id'][0]
        studio = Studio.objects.get(id=studio_id)
        service = Service.objects.get(id=service_id)
        masters = Master.objects.filter(studio=studio, service=service)
        studio_masters={}
        for master in masters:
            profession = Profession.objects.filter(master=master)
            studio_masters[master.id] = {
                'id': master.id,
                'name': master.name,
                'prof': [prof.title for prof in profession],
                'photo_url': master.photo.url
            }
        return JsonResponse(studio_masters) 

