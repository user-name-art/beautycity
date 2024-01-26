from django.shortcuts import render
from beautycityapp.models import Studio, TypeService
from django.http import JsonResponse

from beauty.settings import MIN_SLIDER_COUNT
from .models import Studio, Service, Master, Comment


def show_home_page(request):
    studios = Studio.objects.all()
    services = Service.objects.all()
    masters = Master.objects.all()
    comments = Comment.objects.order_by("-id")[:5]
    return render(
        request,
        "index.html",
        context=dict(
            studios=studios,
            studios_blanks=range(MIN_SLIDER_COUNT - studios.count()),
            services=services,
            services_blanks=range(MIN_SLIDER_COUNT - services.count()),
            masters=masters,
            masters_blanks=range(MIN_SLIDER_COUNT - masters.count()),
            comments=comments,
            comments_blanks=range(MIN_SLIDER_COUNT - comments.count())
        )
    )


def show_service(request):
    studios = Studio.objects.all()
    types_service = TypeService.objects.all()
    context = {
        'studios': studios,
        'types_service': types_service
    }
    return render(
        request,
        "service.html",
        context # todo
    )


def show_admin(request):
    return render(
        request,
        "admin.html",
        context={}  # todo
    )


def show_notes(request):
    return render(
        request,
        "notes.html",
        context={}  # todo
    )


def show_popup(request):
    return render(
        request,
        "popup.html",
        context={}  # todo
    )


def show_service_finally(request):
    return render(
        request,
        "serviceFinally.html",
        context={}  # todo
    )
