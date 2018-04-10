# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 13:53
# @Author  : Tyx
# @Site    : 
# @File    : urls.py.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = "bookTest"

urlpatterns = [
    path("index/",views.index,name="index"),
    path("",views.index,name="index"),
    path("show/<int:id>/",views.show,name="show"),
    path("reverseAnyais/<int:number>/<int:id>",views.reverseAnyais,name="reverseAnyais"),
    path("base/",views.base,name="base"),
    path("baseIndex/",views.baseIndex,name="baseIndex"),
    path("user1/",views.user1,name="user1"),
    path("staticPage/",views.staticPage,name="staticPage"),
    path("uploadFile/",views.uploadFile,name="uploadFile"),
    path("uploadFileHandler/",views.uploadFileHandler,name="uploadFileHandler"),
    path("heroList/<int:pageIndex>",views.heroList,name="heroList")
]

