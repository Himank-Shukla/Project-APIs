from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments
from .models import ChangeReq
from .models import UserDetail
from .models import ArchiveDb
from .models import AddGrp


from django.core.files.storage import default_storage

# Create your views here.
from .serializers import DepartmentSerializer
from .serializers import ChangeReqSerializer
from .serializers import UserDetailSerializer
from .serializers import ArchiveDbSerializer
from .serializers import AddGrpSerializer


@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(ID=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(ID=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)\



@csrf_exempt
def TreqApi(request,id=0):
    if request.method=='GET':
        Treq = ChangeReq.objects.all()
        Treq_serializer=ChangeReqSerializer(Treq,many=True)
        return JsonResponse(Treq_serializer.data,safe=False)
    elif request.method=='POST':
        Treq_data=JSONParser().parse(request)
        Treq_serializer=ChangeReqSerializer(data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Treq_data=JSONParser().parse(request)
        Treq=ChangeReq.objects.get(ID=Treq_data['ID'])
        Treq_serializer=ChangeReqSerializer(Treq,data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        Treq=ChangeReq.objects.get(ID=id)
        Treq.delete()
        return JsonResponse("Deleted Successfully",safe=False)\


@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        user = UserDetail.objects.all()
        Treq_serializer=UserDetailSerializer(user,many=True)
        return JsonResponse(Treq_serializer.data,safe=False)
    elif request.method=='POST':
        Treq_data=JSONParser().parse(request)
        Treq_serializer=UserDetailSerializer(data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Treq_data=JSONParser().parse(request)
        Treq=UserDetail.objects.get(ID=Treq_data['ID'])
        Treq_serializer=UserDetailSerializer(Treq,data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        Treq=UserDetail.objects.get(ID=id)
        Treq.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def ArchiveDbApi(request,id=0):
    if request.method=='GET':
        user = ArchiveDb.objects.all()
        Treq_serializer=ArchiveDbSerializer(user,many=True)
        return JsonResponse(Treq_serializer.data,safe=False)
    elif request.method=='POST':
        Treq_data=JSONParser().parse(request)
        Treq_serializer=ArchiveDbSerializer(data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Treq_data=JSONParser().parse(request)
        Treq=ArchiveDb.objects.get(ID=Treq_data['ID'])
        Treq_serializer=ArchiveDbSerializer(Treq,data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        Treq=ArchiveDb.objects.get(ID=id)
        Treq.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def AddGrpApi(request,id=0):
    if request.method=='GET':
        user = AddGrp.objects.all()
        Treq_serializer=AddGrpSerializer(user,many=True)
        return JsonResponse(Treq_serializer.data,safe=False)
    elif request.method=='POST':
        Treq_data=JSONParser().parse(request)
        Treq_serializer=AddGrpSerializer(data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Treq_data=JSONParser().parse(request)
        Treq=AddGrp.objects.get(ID=Treq_data['ID'])
        Treq_serializer=AddGrpSerializer(Treq,data=Treq_data)
        if Treq_serializer.is_valid():
            Treq_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        Treq=AddGrp.objects.get(ID=id)
        Treq.delete()
        return JsonResponse("Deleted Successfully",safe=False)