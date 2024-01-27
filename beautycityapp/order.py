# from django.http import JsonResponse
from django.http import JsonResponse
from beautycityapp.models import Studio, Service, Master


def make_order(request):
    if request.method == 'POST':
        response = dict(request.POST)
        print(response)
        return JsonResponse({}) 

