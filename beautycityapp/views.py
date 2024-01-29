from django.shortcuts import render, redirect
from beautycityapp.models import Studio, TypeService
from django.http import JsonResponse

from beauty.settings import MIN_SLIDER_COUNT
from .models import Studio, Service, Master, Comment, Client

from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
import random
from django.contrib.auth import get_user_model
from smsru.service import SmsRuApi
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import date


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
        context={}  # todo
    )


def show_admin(request):
    return render(
        request,
        "admin.html",
        context={}  # todo
    )


@login_required
def show_notes(request):
    user = request.user
    orders = user.orders.all()
    sum_cost = 0
    new_orders, old_orders = [], []
    for order in orders:
        print(order.slot.day)
        if order.slot.day >= date.today():
            new_orders.append(order)
            sum_cost += order.cost
        else:
            old_orders.append(order)

    return render(
        request,
        "notes.html",
        context={
                'new_orders': new_orders,
                'old_orders': old_orders,
                'sum_cost': sum_cost,
                'user': user
        }
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


class OTPVerificationView(View):
    def post(self, request):
        submitted_otp = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        password = request.session.get('password')

        if submitted_otp == saved_otp:
            messages.success(request, "OTP verification successful")
            phone_number = request.session.get('phone_number')
            User = get_user_model()
            user = User.objects.create(phone_number=phone_number)
            user.set_password(password)
            user.save()
            return redirect('user_login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('otp_verification')


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(
            request,
            'registration.html',
            {'form': form, 'otp_required': False}
        )

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            phone_number = str(form.cleaned_data['phone_number'])
            verification_method = form.cleaned_data['verification_method']

            if 'otp' in request.POST:
                return OTPVerificationView.as_view()(request)
            else:
                password = form.cleaned_data['password']
                otp = generate_otp()

                if verification_method == 'sms':
                    api = SmsRuApi()
                    result = api.send_one_sms(phone_number, otp)
                    print(result)
                    print(phone_number, otp)

                request.session['otp'] = otp
                request.session['phone_number'] = phone_number
                request.session['password'] = password
                form.fields['password'].widget.attrs['value'] = password

                return render(
                    request,
                    'registration.html',
                    {'form': form, 'otp_required': True, 'password': password}
                )

        return render(
            request,
            'registration.html',
            {'form': form, 'otp_required': False}
        )


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(username=mobile_number, password=password)
            login(request, user)

        return render(request, 'index.html', {'phone_number': mobile_number})


def user_logout(request):
    logout(request)
    return render(request, 'index.html')


def generate_otp():
    return str(random.randint(100000, 999999))
