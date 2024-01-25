from django.shortcuts import render


def show_home_page(request):
    return render(
        request,
        "index.html",
        context={}  # todo
    )


def show_service(request):
    return render(
        request,
        "service.html",
        context={}  # todo
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
