from django.conf.urls import include,url
# from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings
# fro import url

from . import views

urlpatterns=[
    url(r'^teams$',views.departmentApi),
    url(r'^teams/([0-9]+)$',views.departmentApi),

    url(r'^change$',views.TreqApi),
    url(r'^change/([0-9]+)$',views.TreqApi),

    url(r'^userdetails$',views.userApi),
    url(r'^userdetails/([0-9]+)$',views.userApi),

    url(r'^archive$',views.ArchiveDbApi),
    url(r'^archive/([0-9]+)$',views.ArchiveDbApi),

    url(r'^addgrp$',views.AddGrpApi),
    url(r'^addgrp/([0-9]+)$',views.AddGrpApi),

]