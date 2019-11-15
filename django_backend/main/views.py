from django.http import JsonResponse, HttpResponseRedirect
import os
import urllib3
import json
def post_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('valid form')
        else:
            print('invalid form')
            print(form.errors)
    return JsonResponse({"res":"hii"})

def get_data(request):
    url = 'http://localhost:4000/send-notification/'
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    # print(response.data)

    # data = json.dumps(response.data)
    return JsonResponse({"Sent":"f"})
		