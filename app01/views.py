from django.shortcuts import render,HttpResponse,redirect
import requests
from app01 import models
from datetime import date

# Create your views
# here.
oo=models.App01Userinfo
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
def login(request):


    if request.method =="GET":
        return render(request,"login.html")
    # print(request.method)
    # print(user)
    print(request.POST.get("user"))
    print(request.POST.get("pw"))
    User=request.POST.get("user")
    pw=request.POST.get("pw")

    try:
        user=oo.objects.get(name=User)
        if user.password==pw:
            return HttpResponse("登录成功")
        else:
            return render(request,"login.html",{"err_m":"密码错误"})
    except oo.DoesNotExist:
        return HttpResponse("用户不存在")
def GetAll(request):
    datalist=oo.objects.all()
    return render(request,"datalist.html",{"datalist":datalist})
def Info_add(request):
    if request.method=="GET":
        return render(request,'Info_Add.html')
    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    age=request.POST.get('age')
    ct=request.POST.get('at')
    sex=request.POST.get('xb')
    did=request.POST.get('did')
    oo.objects.create(name=user,password=pwd,age=age,account=ct,create_time=date.today(),gender=sex,depart_id=did)
    # return HttpResponse('添加成功')
    return render(request, 'Info_Add.html')
def depart(request):
    return render(request,'depart.html')
def info_delete(request):
    nid=request.GET.get("nid")
    oo.objects.filter(id=nid).delete()
    return redirect('/datalist/')