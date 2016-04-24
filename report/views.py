from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
import json

# Create your views here.


def MSC_Clear_Codes(request):

    return render_to_response('index.html', locals())


@csrf_exempt
def login(request):
    data = json.loads(request.body)
    res = dict()
    if data['username'] == "sam" and data["password"] == "123":
        res['login'] = "success"
    else:
        res['login'] = "failed"

    res = json.dumps(res)
    return HttpResponse(res)
