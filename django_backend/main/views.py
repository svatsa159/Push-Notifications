from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import requests
from main import notifs
from django.shortcuts import redirect
import time
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
    if(os.path.isfile("res1.jpeg")):
        with open("res1.jpeg", "rb") as f:
            encoded_string = base64.b64encode(f.read())
            js = json.dumps({"image":encoded_string,"data":"1"})
            deleteThread().start()
            return JsonResponse(js,safe=False)
    else:
        js = json.dumps({"data":"0"})
        return JsonResponse(js,safe=False)
	