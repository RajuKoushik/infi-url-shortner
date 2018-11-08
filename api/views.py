from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DetailsForm
import requests
import json
import hashlib

import random


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DetailsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print(form.cleaned_data['username'])

            print(int(hashlib.sha1(form.cleaned_data['username'].encode('utf-8')).hexdigest(), 16) % (10 ** 8))
            hash = int(hashlib.sha1(form.cleaned_data['username'].encode('utf-8')).hexdigest(), 16) % (10 ** 8)

            return HttpResponseRedirect('/' + str(hash) + '/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DetailsForm()

    return render(request, 'api/home.html', {'form': form})
