from django.shortcuts import render
from .models import CrudUser
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse


def CrudView(request):
    users=CrudUser.objects.all()
    context={
        'users':users
    }
    return render(request,'crud/list.html',context)

def CreateUser(request):
    name1=request.GET.get('name',None)
    address=request.GET.get('address',None)
    phone=request.GET.get('phone',None)

    obj=CrudUser.objects.create(
        name=name1,
        address=address,
        phone=phone
    )
    user={'id':obj.id,'name':obj.name,'address':obj.address,'phone':obj.phone}
    data={
        'user':user
    }
    return JsonResponse(data)

def UpdateUser(request):
    id1=request.GET.get('id',None)
    name1=request.GET.get('name',None)
    address=request.GET.get('address',None)
    phone=request.GET.get('phone',None)

    obj=CrudUser.objects.get(id=id1)
    obj.name=name1,
    obj.address=address,
    obj.phone=phone
    obj.save()

    user={'id':obj.id,'name':obj.name,'address':obj.address,'phone':obj.phone}
    data={
        'user':user
    }
    return JsonResponse(data)

def DeleteUser(request):
    id1=request.Get.get('id',None)
    CrudUser.objects.get(id=id1).delete()
    data={
        'deleted':True
    }
    return JsonResponse(data)

