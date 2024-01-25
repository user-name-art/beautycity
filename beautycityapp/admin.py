from django.contrib import admin
from beautycityapp.models import Master, Studio, Slot,\
    Service, Client, Order, Comment, Pay

# Register your models here.
admin.site.register(Master)
admin.site.register(Studio)
admin.site.register(Slot)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Pay)