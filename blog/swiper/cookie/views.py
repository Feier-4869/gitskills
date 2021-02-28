from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def send(request):
    # 响应对象
    # Httpresponse
    # render
    # (redirect)
    res=HttpResponse()
    # 创建cookie
    res.set_cookie('usernmae','fei',180)
    return res

def sess(request):
    # 设置session
    # request.session['name']='feier'

    print('sess')

    return HttpResponse('sess')