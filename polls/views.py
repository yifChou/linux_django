from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
from .models import Question,Choice
import random
import json
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
def json_response(data, code=200, ensure_ascii=False, **kwargs):
    data = {
        "code": code,
        "msg": "成功",
        "data": data,
    }
    return JsonResponse(data)

def json_error(error_string="", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return JsonResponse(data)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def Question_insert(request):
    try:
        b={"aaa":123}
        a=b["bbb"]
        print(a)
    except Exception as e:
        print(e)
    # if request.method=="POST":
    #     print("post")
    #     body = eval(request.body)
    #     print(body)
    #     try:
    #         text = body["text"]
    #         createtime = body["createtime"]
    #         Question.objects.create(question_text=text+str(random.randint(1000,9999)),pub_date=timezone.now()).save()
    #         return json_response(data=body)
    #     except Exception as e:
    #         return json_error(error_string=e,code=500)
    # else:
    #     print("no post")
    #     return HttpResponse("no post")
