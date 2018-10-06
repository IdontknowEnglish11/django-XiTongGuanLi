from django.shortcuts import render,redirect
from cmdb import sql_api

# Create your views here.


def login(request):
    msg=''
    if request.method=='GET':
        return render(request, 'login.html')
    else:

        u=request.POST.get('username',None)
        p=request.POST.get('pwd',None)

        if u =='用户名' and p=='密码':
            msg = '账号或密码错误'
        else:
            obj = sql_api.AdminUser(u,p)

            if obj:
                host_obj=sql_api.Userhost()
                return render(request, 'host.html',{'host_obj':host_obj})
            else:
                msg='账号或密码错误'
        return render(request, 'login.html' ,{'msg':msg})

def host(request):
    host_obj = sql_api.Userhost()
    return render(request, 'host.html', {'host_obj': host_obj})


def tang(request):
    ip=request.POST.get('ip',None)
    port=request.POST.get('port',None)
    user=request.POST.get('user',None)
    password=request.POST.get('password',None)
    business=request.POST.get('business',None)
    Asset_group=request.POST.get('Asset_group',None)
    Admin=request.POST.get('Admin',None)
    obj=sql_api.AddUserHost(ip,port,user,password,business,Asset_group,Admin)
    if obj:
        host_obj = sql_api.Userhost()
        return render(request, 'host.html', {'host_obj': host_obj})

def detail(request):
    nid=request.GET.get('nid')
    obj=sql_api.sql_host(nid)
    print(obj)
    if obj:
        return render(request, 'host_detail.html', {'obj': obj})


def deleter(request):
    nid = request.GET.get('nid')
    sql_api.deleter(nid)

    host_obj = sql_api.Userhost()
    return render(request, 'host.html', {'host_obj': host_obj})