import json

from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Book, Hero

# Create your views here.
from django.urls import reverse

# from swiper.user.models import User


def index(request):
    return HttpResponse('ok')


def list(request):
    context={
        'name':'feier',
        'lists':['a','b','c'],
        'dicts':{'A':'aa','B':'bb','C':'cc'}
    }
    return render(request, 'index.html',context)


def info(request,name,age):
    # 按照/传递参数
    print(name)
    print(age)

    return HttpResponse('info')

def infos(request):
    # 按照？传递参数
    # name=request.GET.get('name')
    name=request.GET.getlist('name')

    print(name)
    return HttpResponse('infos')

def posts(request):
    name=request.POST.get('name')
    print(name)
    return HttpResponse('posts')

def puts(request):
    # put方式传递数据格式json
    data=request.body
    # 把字节转成字符串
    data=data.decode()
    # 把ｊｓｏｎ字符串转成字典
    data=json.loads(data)
    print(data,type(data))
    return HttpResponse('puts')

def tourl(request):
    # 静态路由
    # url='/user/index'
    # 生成动态路由（ｎａｍｅ='abc')
    # url=reverse('abc')
    # 命名空间（在总路由里面设置namespace='users'
    url=reverse('users:abc')
    return redirect(url)


def finds(request):

    # user=User.objects.filter(sex='1')
    # user=User.objects.filter(age__gt=150,age__lt=250,sex='1')

    # user=User.objects.filter(name__contains='b')
    # Q代表或者意思
    user=User.objects.filter(Q(sex='1')| Q(age__gt=250))


    # ｉd=3的年龄段加１００
    # user=User.objects.filter(id=3).update(age=F('age')+100)
    # 第二种方法
    # user=User.objects.get(id=4)
    # user.age+=30
    # user.save()


    # id!=3的数据
    # user=User.objects.filter(~Q(id=3))
    user=User.objects.exclude(id=5)


    # id在［４，５］里面的数据
    user=User.objects.filter(id__in=[4,5])
    for u in user:
        print(u)
    return HttpResponse('finds')



def connects(request):
    # 查询图书ｉｄ=1所有英雄的数据

    b =Book.objects.get(id=1)
    h=b.hero.all()
    for i in h:
        print(i)


    # 查询英雄ｉｄ=5的书名
    h=Hero.objects.get(id=5)
    print(h.hbook)

    return HttpResponse('connects')



