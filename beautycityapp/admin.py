from django.contrib import admin

from beautycityapp.models import (
    Master,
    Studio,
    Slot,
    Service,
    Client,
    Order,
    Comment,
    Pay,
    TypeService
)
from .forms import StudioForm, ServiceForm, MasterForm

# Register your models here.
admin.site.register(Slot)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Pay)
admin.site.register(TypeService)


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ("title", "address",)
    search_fields = ("title", "address",)
    form = StudioForm


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    form = MasterForm


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    form = ServiceForm
