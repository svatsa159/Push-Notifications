from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import os
import urllib3
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import requests
from main import notifs
from django.shortcuts import redirect
import time
from django.core.signals import request_finished
from django.dispatch import receiver
from .threads import ProcessThread,deleteThread
import simplejson as json
import base64
@csrf_exempt
def post_upload_view(request):
    if request.method == 'POST':
        print('valid form')
        myfile = request.FILES['myfile']
        # print(os.getcwd())
        fs = FileSystemStorage()
        filename = fs.save("res.jpeg", myfile)
        notifs.notify_users("File uploaded")
        
        ProcessThread().start()
        return redirect("http://35.224.23.154:8080/")

def get_data(request):
    # url = 'http://localhost:4000/send-notification/'
    # http = urllib3.PoolManager()
    # response = http.request('GET', url)
    # print(response.data)
    # notifs.notify_users("Wassup")
    # request_finished.connect(my)
    # data = json.dumps(response.data)
    if(os.path.isfile("res1.jpeg")):
        with open("res1.jpeg", "rb") as f:
            encoded_string = base64.b64encode(f.read())
            js = json.dumps({"image":encoded_string,"data":"1"})
            deleteThread().start()
            return JsonResponse(js,safe=False)
        # except IOError:
        #     red = Image.new('RGBA', (1, 1), (255,0,0,0))
        #     response = HttpResponse(content_type="image/jpeg")
        #     red.save(response, "JPEG")
        #     return response
    else:
        js = json.dumps({"data":"0"})
        return JsonResponse(js,safe=False)
    # return JsonResponse({"Sent":"f"})
	