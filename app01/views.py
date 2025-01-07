from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def index(request):
    return HttpResponse("aaaa")
def user_list(request):
    return render(request,"user_list.html")
def user_add(request):
    return render(request,"user_add.html")
def lianxi(request):
    name="姓名"
    role=["Admin","CEO","保安"]
    infor={"name":"jordan","sl":300,"role":"Boss"}
    res=request.get()
    d_list=[
        {"name": "pipen", "sl": 400, "role": "Boss_pipen"},
        {"name": "rodman", "sl": 500, "role": "Boss_rodam"},
        {"name": "kidd", "sl": 600, "role": "Boss_Kidd"}
    ]
    return render(request,"ee.html",{"n1":name,"n2":role,"n3":infor,"n4":d_list})
