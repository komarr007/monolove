from django.shortcuts import render
from .models import LoveTester
import requests as exter_request
from django.http import HttpResponseRedirect
import json


# Create your views here.
def index(request):
    context = {}

    return render(request, 'index.html', context)

GLOBAL_CONTEXT = {}

# Create your views here.
def match_tester(request):

    context = {}

    if request.method == 'POST':
        if 'lovetester_submit' in request.POST:
        # create a form instance and populate it with data from the request:
            lt_form = LoveTester(request.POST)
            # check whether it's valid:
            if lt_form.is_valid():
        
                context['love_tester_form'] = lt_form.cleaned_data

                json_data = json.dumps(
                    {
                        "data": lt_form.cleaned_data
                    }
                )

                endpoint = "http://127.0.0.1:5000/predict"
                headers = {"content-type": "application/json"}

                response = exter_request.post(endpoint, data=json_data, headers=headers)
                context['prediction'] = json.loads(response.content)['prediction']

                GLOBAL_CONTEXT['prediction'] = context['prediction']

            return HttpResponseRedirect('/results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        lt_form = LoveTester()
        context['love_tester_form'] = lt_form
    
    return render(request, 'match_tester.html', context)

def results(request):
    context = {}

    percentage = GLOBAL_CONTEXT['prediction']*100
    formatted_percentage = "{:.2f}".format(percentage)

    context['value'] = formatted_percentage

    return render(request, 'results.html', context)
