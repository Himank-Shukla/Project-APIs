from rest_framework import serializers
# from EmployeeApp.models import Departments
from .models import Departments
from .models import ChangeReq
from .models import UserDetail
from .models import ArchiveDb
from .models import AddGrp


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('ID','CODE','NAME')

class ChangeReqSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChangeReq
        fields=('ID','FNAME','LNAME','OLDTEAM','NEWTEAM','MANAGER','COMMENTS','APPROVAL')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetail
        fields=('ID'	,'UEID',	'LDAP_USERNAME'	,'LOGIN'	,'GROUPID'	,'FIRST_NAME',	'LAST_NAME'	,'DISP_NAME'	,'SHORT_NAME','EMAIL','ADMIN')

class ArchiveDbSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDb
        fields=('ID','UID','GROUP','START','END','WOR','APPROVAL')

class AddGrpSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddGrp
        fields=('ID','UID','USERNAME','GROUP','HIDDEN','APPROVAL')