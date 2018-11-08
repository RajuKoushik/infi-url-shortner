from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DetailsForm
import requests
import json
import hashlib

import random



