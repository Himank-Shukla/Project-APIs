from django.db import models
# Create your models here.
class Departments(models.Model):
    ID = models.AutoField(primary_key=True)
    CODE = models.CharField(max_length=50)
    NAME = models.CharField(max_length=500)

class ChangeReq(models.Model):
    ID = models.AutoField(primary_key=True)
    FNAME = models.CharField(max_length=500)
    LNAME = models.CharField(max_length=500)
    OLDTEAM = models.CharField(max_length=500)
    NEWTEAM = models.CharField(max_length=500)
    MANAGER = models.CharField(max_length=500)
    COMMENTS = models.CharField(max_length=5000)
    APPROVAL = models.IntegerField()

class UserDetail(models.Model):
    ID = models.AutoField(primary_key=True)
    UEID = models.IntegerField()
    LDAP_USERNAME = models.CharField(max_length=500)
    LOGIN = models.CharField(max_length=500)
    GROUPID = models.IntegerField()
    FIRST_NAME = models.CharField(max_length=500)
    LAST_NAME = models.CharField(max_length=500)
    DISP_NAME = models.CharField(max_length=500)
    SHORT_NAME = models.CharField(max_length=500)
    EMAIL = models.CharField(max_length=500)
    ADMIN = models.IntegerField(default=0)



class ArchiveDb(models.Model):
    ID = models.AutoField(primary_key=True)
    UID = models.IntegerField()
    GROUP = models.CharField(max_length=500)
    START = models.DateField()
    END = models.DateField()
    WOR = models.CharField(max_length=500)
    APPROVAL = models.IntegerField(default=-1)

class AddGrp(models.Model):
    ID = models.AutoField(primary_key=True)
    UID = models.IntegerField()
    USERNAME = models.CharField(max_length=500)
    GROUP = models.CharField(max_length=500)
    HIDDEN = models.IntegerField()
    APPROVAL = models.IntegerField(default=-1)
