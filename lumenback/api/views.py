from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import librosa
from django import forms
from . import predict, learn
from django.conf import settings
from django.urls import resolve
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from copy import copy

instruments = {
    "cel" : 0 ,
    "cla" : 0 ,
    "flu" : 0 ,
    "gac" : 0 ,
    "gel" : 0 ,
    "org" : 0 ,
    "pia" : 0 ,
    "sax" : 0 ,
    "tru" : 0 ,
    "vio" : 0 ,
    "voi" : 0
}

def print_trusted_origins(request):
    try:
        trusted_origins = settings.CORS_ORIGIN_WHITELIST
        response = "Trusted Origins: " + ', '.join(trusted_origins)
        return HttpResponse(response)
    except:
        return HttpResponse("All")
    

def index(request):
    return render(request, "index.html")

#@api_view(['POST'])
@csrf_exempt
def processFile(request):
    if request.method == 'POST' and "file" in request.FILES:
        file = request.FILES["file"]
        try:
            y, sr = librosa.load(file)
        except:
            return(HttpResponseBadRequest("Not a song!"))
        
        response = copy(instruments)
        for i in predict(learn, y, sr):
            response[i] = 1
        return JsonResponse(response)
        
    return(HttpResponseBadRequest("No file!"))