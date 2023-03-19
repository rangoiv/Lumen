from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
import requests
import librosa
from IPython.display import Audio
from django.http import JsonResponse

def home(request):
    #data = request.POST.get('name')
    if request.method == "POST":
        file = request.FILES["file"]
        print(type(file.file))
        if str(file.name).endswith(".wav"):
            print("DATA", file)
            y, sr = librosa.load(file, sr=None)

            response_data = {
                "file_name": file.name,
                "file_type": file.content_type,
                "file_size": file.size,
                "duration": librosa.get_duration(y=y, sr=sr),
                "sampling_rate": sr
            }
            return JsonResponse(response_data)
        return HttpResponse("file not .wav!")
    
    return render(request,'index.html')

@api_view(['GET'])
def getData(request):
    person = {'name':"luka", 'age':22}
    return Response(person)

@api_view(['POST'])
def postData(request):
    data = request.POST.get('name')
    print("POST:", data)
    return Response(data)