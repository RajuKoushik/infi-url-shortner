from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DetailsForm
import requests
import json
import hashlib

from .models import Url
import random
from . import models


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

            url = models.Url()
            url.old_url = form.cleaned_data['username']
            url.new_url = hash
            url.save()
            print(url.new_url)

            url_all = Url.objects.all()
            print((url_all))
            return render(request, 'api/home.html', {'url': hash, 'form': form, 'model':url_all})

    else:
        form = DetailsForm()

    return render(request, 'api/home.html', {'form': form})
