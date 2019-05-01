from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
from polls.forms import RequestModelForm
from polls.models import Dayoff


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        print(username, password, user)
        if user:
            auth.login(request, user)
            if user.groups.filter(name='HR Manager').exists():
                return redirect('/admin/polls/dayoff/')
            return redirect('index')

        context['username'] = username
        context['password'] = password
        context['error'] = "username or password incorrect"

    return render(request, template_name='polls/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def index(request):
    context = {}
    user = request.user
    alldayoff = Dayoff.objects.filter(create_by=user)
    context['alldayoff'] = alldayoff
    return render(request, template_name='polls/index.html', context=context)

@login_required
def dayoff(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        form = RequestModelForm(request.POST)
        if form.is_valid():
            Dayoff.objects.create(
                create_by=user,
                reason=form.cleaned_data.get('reason'),
                type=form.cleaned_data.get('type'),
                date_start=form.cleaned_data.get('date_start'),
                date_end=form.cleaned_data.get('date_end'),
            )
            context['success'] = 'Request successfully submitted'
        print(form)

    else:
        form = RequestModelForm()

    context['form'] = form
    return render(request, template_name='polls/dayoff.html', context=context)
