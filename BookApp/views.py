from django.shortcuts import render
from .models import *
from django.http import *
import os
from django.conf import settings
from django.core.paginator import *
import time
# from django.template import RequestContext,loader
# Create your views here.

def index(request):
    # temp = loader.get_template("BookApp/index.html")
    # temp.render()
    # return HttpResponse("<h1>你好</h1>")
    # return HttpResponse(temp.render())
    # dataContext = {"title":"hello"}
    dataist = BookInfo.objects.all()
    hero = HeroInfo.objects.get(pk=1)
    dataContext = {"dataList":dataist,"hero":hero}
    return render(request,"BookApp/index.html",dataContext)

def show(request,id):
    bookInfo = BookInfo.objects.get(pk=id)
    hereInfos = bookInfo.heroinfo_set.all()
    if hereInfos == None:
        hereInfos = []
    dataContext = {"hereInfos":hereInfos}
    return render(request,"BookApp/Show.html",dataContext)

# 反向解析
def reverseAnyais(request,number,id):
    context = {"number":number}
    return render(request,"BookApp/reverseAnyais.html",context)

# 模板继承
def base(request):
    return render(request,"BookApp/base.html")

def baseIndex(request):
    return render(request,"BookApp/baseIndex.html")

def user1(request):
    return render(request,"BookApp/user1.html")

# 静态文件
def staticPage(request):
    return render(request,"BookApp/staticPage.html")

# 上传文件
def uploadFile(request):
    return render(request,"BookApp/uploadFiles.html")

def uploadFileHandler(request):
    if request.method == "POST":
        updloadPic = request.FILES["pic"]
        uploadFile = os.path.join(settings.MEDIA_ROOT,updloadPic.name)
        with open(uploadFile,"wb") as picture:
            for i in updloadPic.chunks():
                picture.write(i)
        return HttpResponse(updloadPic.name)
    else:
        return HttpResponse("error")

# 分页
def heroList(request,pageIndex=1):

    heros = HeroInfo.objects.all()
    paginator = Paginator(heros,5) # 参数一集合，参数二 pageSize
    page = paginator.page(pageIndex) #
    context = {"page":page}
    return render(request,"BookApp/heroList.html",context)