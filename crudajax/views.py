from django.shortcuts import render
from .models import CrudUser
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def index(request):
    users=CrudUser.objects.all()
    return render(request,'crud/list.html',{'users':users})

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        obj=CrudUser.objects.create(
            name=name,address=address,phone=phone
        )
        return JsonResponse(model_to_dict(obj),safe=False)

def update(request):
    if request.method=='POST':
        id1=request.POST.get('id')
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
            
        obj=CrudUser.objects.get(id=id1)
        obj.name=name
        obj.address=address
        obj.phone=phone
        
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'phone':obj.phone}

        data = {
                'user': user
            }
        print(data)
        return JsonResponse(data)

def delete(request):
    id1 = request.GET.get('id', None)
    CrudUser.objects.get(id=id1).delete()
    data = {
            'deleted': True
        }
    return JsonResponse(data)