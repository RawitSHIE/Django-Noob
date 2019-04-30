from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from polls.forms import RequestModelForm
from polls.models import Dayoff


def index(request):
    return render(request, template_name='polls/index.html', context={})

def dayoff(request):
    context = {}
    if request.method == 'POST':
        form = RequestModelForm(request.POST)
        if form.is_valid():
            Dayoff.objects.create(
                reason=form.cleaned_data.get('reason'),
                type=form.cleaned_data.get('type'),
                date_start=form.cleaned_data.get('date_start'),
                date_end=form.cleaned_data.get('date_end'),
            )
        success = 'Request successfully submitted'
    else:
        form = RequestModelForm()
        success = 'Not done with you yet'
    context['form'] = form
    context['success'] = success
    return render(request, template_name='polls/request_dayoff.html', context=context)