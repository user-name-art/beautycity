
# from django.http import JsonResponse
from django.http import JsonResponse
from beautycityapp.models import Slot, Master


def get_slots(request):
    if request.method == 'POST':
        response = dict(request.POST)
        print(response)
        master_id = response['master_id'][0]
        selected_day = response['selected_day'][0]
        master = Master.objects.get(id=master_id)
        slots = Slot.objects.filter(master=master, day=selected_day).order_by('time')
        master_slots = {}
        for count, slot in enumerate(slots):
            master_slots[count] = {
                'id': slot.id,
                'time': str(slot.time)[:-3],
            }
        return JsonResponse(master_slots) 