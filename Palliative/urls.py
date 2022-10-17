"""Palliative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.conf import settings

urlpatterns = [

    #public section
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('mission/',views.mission),
    path('services/',views.services),
    path('contact/',views.contact),
    path('form/',views.form),
    path('header/',views.header),
    path('indexheader/',views.indexheader),
    path('login/',views.login),
    path('contactus/',views.contactus),
    path('smssend/',views.smssend),
    path('log/',views.log),
    path('reg_volunteer/',views.reg_volunteer),
    path('regvolunteer/',views.regvolunteer),
    path('add_volunteer/',views.add_volunteer),
    path('add_volunteer1/',views.add_volunteer1),
    path('reg_patient/',views.reg_patient),
    path('regpatient/',views.regpatient),
    path('donation/',views.donation),
    path('regdonation/',views.regdonation),
    #end of public section

    #admin
    path('admins/',views.admins),
    path('add_zone/',views.add_zone),
    path('addzone/',views.addzone),
    path('remove_zone/',views.remove_zone),
    path('removezone/<str:id>',views.removezone),
    path('verify_volunteer/',views.verify_volunteer),
    path('verify/<str:id>',views.verify),
    path('reject/<str:id>',views.reject),
    path('remove_volunteer/',views.remove_volunteer),
    path('removevlounteer/<str:id>',views.removevlounteer),
    path('viewdonation/',views.viewdonation),
    path('accept/<str:Donationid>',views.accept),
    path('adminreport/',views.adminreport),
    path('request/<str:id>',views.request),
    path('complaint/<str:id>',views.complaint),
    path('viewupdate/',views.viewupdate),
    path('logout/',views.logout),


    #end of admin section

    #zone
    path('zone/',views.zone),
    path('add_clinic/',views.add_clinic),
    path('addclinic/',views.addclinic),
    path('remove_clinic/',views.remove_clinic),
    path('removeclinic/<str:id>',views.removeclinic),
    path('view_clinic/',views.view_clinic),
    path('update_clinic/<str:id>',views.update_clinic),
    path('updateclinic/<str:id>',views.updateclinic),
    path('volunteer_clinic_allotment/',views.volunteer_clinic_allotment),
    path('volunteerclinicallotment/<str:id>',views.volunteerclinicallotment),
    path('updatevolunteerclinicallotment/<str:id>',views.updatevolunteerclinicallotment),


    #end of zone

    #patient

    path('patient/',views.patient),
    path('generate_request/',views.generate_request),
    path('generaterequest/',views.generaterequest),
    path('givecomplaint/',views.givecomplaint),
    path('insertcomplaint/',views.insertcomplaint),
    path('givereview/',views.givereview),
    path('insertreview/',views.insertreview),

    #end of patient

    #clinic

    path('clinic/',views.clinic),
    path('process_request/',views.process_request),
    path('allot_volunteer/<str:rqid>',views.allot_volunteer),
    path('allotvolunteer/<str:rqid>',views.allotvolunteer),
    path('view_volunteer_status/',views.view_volunteer_status),
    path('view_volunteer_status1/',views.view_volunteer_status1),
    path('allotvolunteerreq/<str:rqid>',views.allotvolunteerreq),
    path('updatestatus/',views.updatestatus),
    path('update/<str:rqid>',views.update),
    path('updating/',views.updating),
    

    #end of clinic

    #volunteer

    path('volunteer/',views.volunteer),
    path('view_volunteer_allotment/',views.view_volunteer_allotment),
    path('acceptallot/<str:id>',views.acceptallot),
    path('rejectallot/<str:id>',views.rejectallot),
    path('process_volunteer_request/<str:id>',views.process_volunteer_request),
    path('processvolunteerrequest/<str:id>',views.processvolunteerrequest),


]
