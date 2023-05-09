from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import librosa
from copy import copy
from django.conf import settings
from api.main import predict, predict_multi, sample_rate
from api.convert import run_only_once

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

#@api_view(['POST'])
@csrf_exempt
def processFile(request):
    if request.method == 'POST' and "file" in request.FILES:
        file = request.FILES["file"]
        try:
            y, sr = librosa.load(file)
            y = librosa.resample(y, orig_sr=sr, target_sr=sample_rate)
        except:
            return(HttpResponseBadRequest("Not a song!"))
        response = copy(instruments)
        for i, j in enumerate(predict_multi(settings.LEARN, [y])[0][0]):
            if j:
                response[settings.LEARN.dls.vocab[i]] = 1
        return JsonResponse(response)
        
    return(HttpResponseBadRequest("No file!"))