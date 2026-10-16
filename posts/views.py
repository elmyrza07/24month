from datetime import timezone

from django.http import HttpRequest
from django.utils import timezone
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def post_list(request):
    return HttpResponse("Hello, World!")

def data(request: HttpRequest):
    timezone.now()
    today = timezone.now()
    return HttpResponse(today)