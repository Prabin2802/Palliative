from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
import datetime
from twilio.rest import Client
from App.models import tbl_help_request, tbl_idgen, tbl_login, tbl_patient_reg, tbl_volunteer, tbl_clinic, tbl_volunteer_allot, tbl_zone,tbl_donation,tbl_complaint,tbl_review,tbl_update

#public 
def index(request):
    return render(request,"index.html")

def mission(request):
    return render(request,"mission.html")

def blog(request):
    return render(request,"blog.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"loginnew.html")
def contactus(request):
    return render(request,"contactus.html")
def smssend(request):
    account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
    auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
    client = Client(account_sid, auth_token)
    phone="6238049406"
    message = client.messages.create(
            body='User Registration Sucessfull!!!\nYour user ID is ',
            from_='+13393296936',
            to='+91'+phone
        )

    print(message.sid) 
    return render(request,"sms.html",{ })
def log(request):
    if request.method == 'POST':
        data=tbl_login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')

        flag=0

        for da in data:
            if un == da.username and pwd == da.password:
                type=da.role
                
                flag=1
                if type=="admin":
                    request.session['uid']=un
                    return render(request,"admin.html")
                elif type=="Patient":
                    request.session['puid']=un
                    return render(request,"patient.html")
                elif type=="Zone":
                    request.session['zuid']=un
                    return render(request,"zone.html")
                elif type=="Volunteer":
                    request.session['vuid']=un
                    return render(request,"volunteer.html")
                elif type=="Clinic":
                    request.session['cuid']=un
                    return render(request,"clinic.html")
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")
def logout(request):
    del request.session['uid']
    return redirect('/index')

def form(request):
    return render(request,"form.html")

def header(request):
    return render(request,"header.html")

def indexheader(request):
    return render(request,"indexheader.html")

def reg_volunteer(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.vid
    id = str(id+1)
    vid = "VID_00" + str(id)
    request.session['vid'] = id
    data1 = tbl_clinic.objects.all()
    return render(request,"reg_volunteer.html",{'vid':vid,'data':data1})

def add_volunteer(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.vid
    id = str(id+1)
    vid = "VID_00" + str(id)
    request.session['vid'] = id
    data1 = tbl_clinic.objects.all()
    return render(request,"add_volunteer.html",{'vid':vid,'data5':data1})    

def reg_patient(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.pid
    id = str(id+1)
    pid = "PID_00" + str(id)
    request.session['pid'] = id
    data1 = tbl_clinic.objects.all()
    return render(request,"reg_patient.html",{'pid':pid,'data':data1})

def donation(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.donid
    id = str(id+1)
    donid = "DONID_00" + str(id)
    request.session['donid'] = id
    return render(request,"donation.html",{'donid':donid})

#form

def regvolunteer(request):
    if request.method == "POST":
        data = tbl_volunteer()
        data.volunteer_id = request.POST.get("txtVolunteerID")
        data.name = request.POST.get("txtName")
        data.age = request.POST.get("txtAge")
        data.gender = request.POST.get("slcGender")
        data.address = request.POST.get("txtAddress")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.city = request.POST.get("txtCity")
        data.location = request.POST.get("txtLocation")
        data.clinic_id_id = request.POST.get("slcZone")
        data2=tbl_clinic.objects.get(clinic_id=request.POST.get('slcZone'))
        data.zone_id_id=data2.zone_id_id
        data.status = "Pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.vid = request.session['vid']
        data1.save()
        
        return render(request,"index.html",{'data':1})
def add_volunteer1(request):
    if request.method == "POST":
        data = tbl_volunteer()
        data.volunteer_id = request.POST.get("txtVolunteerID")
        data.name = request.POST.get("txtName")
        data.age = request.POST.get("txtAge")
        data.gender = request.POST.get("slcGender")
        data.address = request.POST.get("txtAddress")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.city = request.POST.get("txtCity")
        data.location = request.POST.get("txtLocation")
        data.clinic_id_id = request.POST.get("slcZone")
        data2=tbl_clinic.objects.get(clinic_id=request.POST.get('slcZone'))
        data.zone_id_id=data2.zone_id_id
        data.status = "Accepted"
        data.save()
        data2 = tbl_login()
        data2.username = data.volunteer_id
        data2.password  = data.phone
        data2.role = "Volunteer"
        data2.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.vid = request.session['vid']
        data1.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone=data.phone
        message = client.messages.create(
            body='User Registration Sucessfull!!!'+'username is :'+data.volunteer_id+'password is :'+data.phone,
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 


        return render(request,"add_volunteer.html",{'data':1})    

def regpatient(request):
    if request.method == "POST":
        data = tbl_patient_reg()
        data.patient_id = request.POST.get("txtPatientID")
        data.name = request.POST.get("txtName")
        data.age = request.POST.get("txtAge")
        data.gender = request.POST.get("slcGender")
        data.address = request.POST.get("txtAddress")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.location = request.POST.get("txtLocation")
        data.clinic_id_id = request.POST.get("slcClinic")
        data2=tbl_clinic.objects.get(clinic_id=request.POST.get('slcClinic'))
        data.zone_id_id=data2.zone_id_id
        data.status = "Active"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.pid = request.session['pid']
        data1.save()

        data2 = tbl_login()
        data2.username = data.patient_id
        data2.password  = data.phone
        data2.role = "Patient"
        data2.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone=data.phone
        message = client.messages.create(
        body='User Registration Sucessfull!!!\nYour user ID is '+data.patient_id+'\n Password is '+data.phone,
        from_='+13393296936',
        to='+91'+phone
        )
        print(message.sid) 


        return render(request,"index.html",{'data':1})

def regdonation(request):
    if request.method == "POST":
        data = tbl_donation()
        data.Donationid = request.POST.get("donationid")
        data.Donationname = request.POST.get("donationname")
        data.Address = request.POST.get("address")
        data.Phonenumber = request.POST.get("phone")
        data.Email = request.POST.get("email")
        data.Itemdescription = request.POST.get("description")
        data.Itemname = request.POST.get("name")
        data.Donationdate=datetime.datetime.now().strftime ("%d-%m-%Y")
        data.status = "Pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.donid = request.session['donid']
        data1.save()
        return render(request,"index.html",{'data':1})

#end of form

#end of public

#admin

def admins(request):
    if 'uid' not in request.session:
        return render(request,'loginnew.html')
    else:
        return render(request,"admin.html")

def add_zone(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.zid
    id = str(id+1)
    zid = "ZID_00" + str(id)
    request.session['zid'] = id
    request.session['zid1']=zid
    return render(request,"add_zone.html")

def remove_zone(request):
    data = tbl_zone.objects.all()
    return render(request,"remove_zone.html",{'data':data})

def remove_volunteer(request):
    data = tbl_volunteer.objects.all()
    return render(request,"remove_volunteer.html",{'data':data})

def verify_volunteer(request):
    data = tbl_volunteer.objects.filter(status = "Pending")
   

    return render(request,"verify_adm_volunteer.html",{'data':data})

def viewdonation(request):
    data=tbl_donation.objects.filter(status="Pending")
    return render(request,"viewdonation.html",{'data':data})

def adminreport(request):
    data=tbl_patient_reg.objects.all()
    return render(request,"adminreport.html",{'data':data})

def request(request,id):
    data =tbl_help_request.objects.filter(patient_id=id)
    return render(request,"request.html",{'data':data})

def complaint(request,id):
    data =tbl_complaint.objects.filter(patient_id=id)
    return render(request,"complaint.html",{'data':data})

def viewupdate(request):
    data=tbl_update.objects.all()
    return render(request,"viewupdate.html",{'data':data})
#form 

def addzone(request):
    if request.method == "POST":
        data = tbl_zone()
        data.zone_id =request.session['zid1']
        data.zone = request.POST.get("txtZone")
        data.authority_name = request.POST.get("txtAuthorityName")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.status = "Active"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.zid = request.session['zid']
        data1.save()

        data2 = tbl_login()
        data2.username = data.zone_id
        data2.password  = data.phone
        data2.role = "Zone"
        data2.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone=data.phone
        message = client.messages.create(
            body='User Registration Sucessfull!!!\nYour user ID is '+data.zone_id+'  \n Your Password is  '+data.phone,
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 

        return render(request,"add_zone.html",{'data':1})

def verify(request,id):
    if request.method == "POST":
        data = tbl_volunteer.objects.get(volunteer_id = id)
        data.status = "Accepted"
        data.save()
        data2 = tbl_login()
        data2.username = data.volunteer_id
        data2.password  = data.phone
        data2.role = "Volunteer"
        data2.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone=data.phone
        message = client.messages.create(
            body='User Registration Sucessfull!!!\nYour user ID is '+data.volunteer_id +' \n Your Password is '+data.phone,
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 

        return redirect("/verify_volunteer")

def reject(request,id):
    if request.method == "POST":
        data = tbl_volunteer.objects.get(volunteer_id = id)
        data.status = "rejected"
        data.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone=data.phone
        message = client.messages.create(
            body='User Registration rejected!!!\n ',
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 

        return redirect("/verify_volunteer")

def accept(request,Donationid):
    if request.method == "POST":
        data = tbl_donation.objects.get(Donationid = Donationid)
        data.status = "Accepted"
        data.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone = data.Phonenumber
        message = client.messages.create(
            body=' Thank You so much for Your generous donation.\n ',
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 

        return redirect("/viewdonation") 
#end of form

#remove

def removezone(request,id):
    data = tbl_zone.objects.get(zone_id = id)
    data.delete()

    data2 = tbl_login.objects.get(username = id)
    data2.delete()
    data = tbl_zone.objects.all()
    return render(request,"remove_zone.html",{'data':data,'data1':1})

def removevlounteer(request,id):
    data = tbl_volunteer.objects.get(volunteer_id = id)
    data.delete()

    data2 = tbl_login.objects.get(username = id)
    data2.delete()
    return redirect("/remove_volunteer")

#end of remove
#end of admin section

#zone section

def zone(request):
    if 'zuid' not in request.session:
        return render(request,'loginnew.html')
    else:
        return render(request,"zone.html")

def add_clinic(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.cid
    id = str(id+1)
    cid = "CID_00" + str(id)
    request.session['cid'] = id
    data1 = tbl_zone.objects.all()
    return render(request,"add_clinic.html",{'data':data1,'cid':cid})

def remove_clinic(request):
    data = tbl_clinic.objects.all()
    return render(request,"remove_zone_clinic.html",{'data':data})

def view_clinic(request):
    data = tbl_clinic.objects.all()
    return render(request,"view_zone_clinic.html",{'data':data})

def update_clinic(request,id):
    data = tbl_clinic.objects.get(clinic_id = id)
    data1 = tbl_zone.objects.all()
    return render(request,"update_zone_clinic.html",{'data':data,'data1':data1})

def volunteer_clinic_allotment(request):
    data = tbl_volunteer.objects.filter(zone_id_id = request.session['zuid'])
    return render(request,"volunteer_zone_clinic_allotment.html",{'data':data})

def volunteerclinicallotment(request,id):
    data = tbl_volunteer.objects.get(volunteer_id = id)
    data1 = tbl_clinic.objects.filter(zone_id = data.zone_id_id)
    return render(request,"volunteer_zoneclinicallotment.html",{'data':data,'data1':data1})
    


#form 

def addclinic(request):
    if request.method=="POST":
        data = tbl_clinic()
        data.clinic_id = request.POST.get("txtClinicID")
        data.zone_id_id = request.POST.get("slcZone")
        data.clinic_name = request.POST.get("txtClinicName")
        data.contact_person = request.POST.get("txtContactPerson")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.status = "Active"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.cid = request.session['cid']
        data1.save()
        
        data2 = tbl_login()
        data2.username = data.clinic_id
        data2.password  = data.phone
        data2.role = "Clinic"
        data2.save()
        account_sid = 'AC08f5b88cd67e367aa93b6b8353d18e53'
        auth_token = 'ee3e13699b5457bea9b21f962a858bd7'
        client = Client(account_sid, auth_token)
        phone = data.phone
        message = client.messages.create(
            body='User Registration Sucessfull!!!\nYour user ID is '+data.clinic_id+'\n Your Password is '+data.phone,
            from_='+13393296936',
            to='+91'+phone
        )
        print(message.sid) 

        return redirect("/add_clinic")

def updateclinic(request,id):
    if request.method=="POST":
        data = tbl_clinic.objects.get(clinic_id = id)
        data.clinic_id = request.POST.get("txtClinicID")
        data.zone_id_id = request.POST.get("slcZone")
        data.clinic_name = request.POST.get("txtClinicName")
        data.contact_person = request.POST.get("txtContactPerson")
        data.phone = request.POST.get("txtPhone")
        data.email = request.POST.get("txtEmail")
        data.status = "Active"
        data.save()

        data2 = tbl_login.objects.get(username = id)
        data2.username = data.clinic_id
        data2.password  = data.phone
        data2.role = "Clinic"
        data2.save()
        return redirect("/view_clinic")

def updatevolunteerclinicallotment(request,id):
    if request.method=="POST":
        data = tbl_volunteer.objects.get(volunteer_id = id)
        data.clinic_id_id = request.POST.get("slcClinic")
        data.save()

        return redirect("/volunteer_clinic_allotment")

#end of form

#remove

def removeclinic(request,id):
    data = tbl_clinic.objects.get(clinic_id = id)
    data.delete()

    data2 = tbl_login.objects.get(username = id)
    data2.delete()
    return redirect("/remove_clinic")

#end of zone section 

#patient 

def patient(request):
    if 'puid' not in request.session:
        return render(request,'loginnew.html')
    else:
        return render(request,"patient.html")

def generate_request(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.rid
    id = str(id+1)
    rid = "RID_00" + str(id)
    request.session['rid'] = id
    data2=request.session['puid']
    data1 = tbl_patient_reg.objects.get(patient_id=data2)
    return render(request,"generate_patient_request.html",{'data':data1,'rid':rid})

#form

def generaterequest(request):
    if request.method == "POST":
        data = tbl_help_request()
        data.request_id = request.POST.get("txtRequestID")
        data.patient_id_id =request.session['puid']
        data.request_dt = request.POST.get("dtDate")
        data.request_type = request.POST.get("type")
        data2=tbl_patient_reg.objects.get(patient_id=request.session['puid'])
        data.zone_id_id=data2.zone_id_id
        data.clinic_id_id=data2.clinic_id_id
        data.request = request.POST.get("txtRequest")
        data.status = "Pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.rid = request.session['rid']
        data1.save()

        return redirect("/patient")

def givecomplaint(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.comid
    id = str(id+1)
    comid = "COMID_00" + str(id)
    request.session['comid'] = id
    data2=request.session['puid']
    return render(request,"givecomplaint.html",{'data':data2,'comid':comid})

def insertcomplaint(request):
    if request.method == "POST":
        data = tbl_complaint()
        data.Complaintid = request.POST.get("complaintid")
        data.patient_id_id =request.POST.get('txtPatientID') 
        data.Complaintdate = request.POST.get("dtDate")
        data.Complaint=request.POST.get("complaint")
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.comid = request.session['comid']
        data1.save()

        return redirect("/patient")

def givereview(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.revid
    id = str(id+1)
    revid = "REVID_00" + str(id)
    request.session['revid'] = id
    data2=request.session['puid']
    return render(request,"givereview.html",{'data':data2,'revid':revid})

def insertreview(request):
    if request.method == "POST":
        data = tbl_review()
        data.Reviewid = request.POST.get("reviewid")
        data.patient_id_id =request.POST.get('txtPatientID') 
        data.Reviewdate = request.POST.get("dtDate")
        data.Review=request.POST.get("review")
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.revid = request.session['revid']
        data1.save()

        return redirect("/patient")
##end of form
#end of patient

#clinic 

def clinic(request):
    if 'cuid' not in request.session:
        return render(request,'loginnew.html')
    else:
        return render(request,"clinic.html")

def process_request(request):
    print(request.session['cuid'])
    data = tbl_help_request.objects.filter(status ="Pending").filter(clinic_id_id=request.session['cuid'])
    return render(request,"process_request.html",{'data':data})

def allot_volunteer(request,rqid):
    data2 = tbl_help_request.objects.get(request_id = rqid)
    data = tbl_volunteer.objects.filter(clinic_id = data2.clinic_id_id).filter(status="Accepted")
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.aid
    id = str(id+1)
    aid = "AID_00" + str(id)
    request.session['aid'] = id
    return render(request,"allot_volunteer.html",{'data':data,'aid':aid,'rqid':rqid})

def view_volunteer_status(request):
    data = tbl_help_request.objects.filter(clinic_id_id=request.session['cuid'])
    return render(request,"view_clinic_volunteer_status.html",{'data':data})
def view_volunteer_status1(request):
    data = tbl_help_request.objects.filter(clinic_id_id=request.session['cuid']).filter(status="Rejected")
    return render(request,"view_clinic_volunteer_status1.html",{'data':data})


def allotvolunteerreq(request,rqid):
    c = tbl_volunteer_allot.objects.filter(request_id_id = rqid).count()
    if c==0:
        return HttpResponse("no request .........")
    else:

        data = tbl_volunteer_allot.objects.get(request_id_id = rqid)
        return render(request,"allotvolunteerreq.html",{'data':data})



#form

def allotvolunteer(request,rqid):
    if request.method == "POST":
        data = tbl_volunteer_allot()
        data.allot_id = request.POST.get("txtAllotID")
        data1 = tbl_help_request.objects.get(request_id = rqid)
        data.volunteer_id_id = request.POST.get("slcVolunteer")
        data.allot_dt =datetime.datetime.now().strftime ("%Y-%m-%d")
        data.request_id_id = data1.request_id
        data.patient_id_id = data1.patient_id_id
        data.comment = request.POST.get("txtComment")
        data.status = "passtovolunteer"
        data.updates = ""
        data.save()
        data1.status="passtovolunteer"
        data1.save()
    
        data2 = tbl_idgen.objects.get(id=1)
        data2.aid = request.session['aid']
        data2.save()

        return redirect("/clinic")

def updatestatus(request):
    data=tbl_help_request.objects.filter(status="Accepted")
    return render(request,"updatestatus.html",{'data':data})

def update(request,rqid):
    data3=tbl_help_request.objects.get(request_id=rqid)
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.upid
    id = str(id+1)
    upid = "UPID_00" + str(id)
    request.session['upid'] = id
    request.session['p']=data3.patient_id_id
    request.session['r']=data3.request_id
    return render(request,"update.html",{'upid':upid})

def updating(request):
    if request.method == "POST":
        data = tbl_update()
        data.Updateid = request.POST.get("updateid")
        data.patient_id_id =request.session['p']
        data.request_id_id =request.session['r']
        data.Requirement=request.POST.get("requirement")
        data.Updatestatus=request.POST.get("status")
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.upid = request.session['upid']
        data1.save()

        return redirect("/updatestatus")


#end of form
#end of clinic

#volunteer

def volunteer(request):
    if 'vuid' not in request.session:
        return render(request,'loginnew.html')
    else:
        return render(request,"volunteer.html")

def view_volunteer_allotment(request):
    data=tbl_volunteer_allot.objects.filter(volunteer_id=request.session['vuid']).filter(status="passtovolunteer")
    return render(request,"view_volunteer_allotment.html",{'data':data})

def acceptallot(request,id):
    if request.method == "POST":
        data = tbl_volunteer_allot.objects.get(allot_id = id)
        data2=tbl_help_request.objects.get(request_id=data.request_id_id)
        data2.status="Accepted"
        data2.save()
        data.status = "Accepted"
        data.save()
        return redirect("/view_volunteer_allotment")

def rejectallot(request,id):
    if request.method == "POST":
        data = tbl_volunteer_allot.objects.get(allot_id = id)
        data2=tbl_help_request.objects.get(request_id=data.request_id_id)
        data2.status="Rejected"
        data2.save()
        data.status = "Rejected"
        data.save()
        return redirect("/view_volunteer_allotment")


def process_volunteer_request(request,id):
    data = tbl_volunteer_allot.objects.get(allot_id = id)
    return render(request,"process_volunteer_request.html",{'data':data})

#form

def processvolunteerrequest(request,id):
    if request.method == "POST":
        data = tbl_volunteer_allot.objects.get(allot_id = id)
        data.updates = request.POST.get("txtUpdates")
        data.save()
        return redirect("/view_volunteer_allotment")

# Create your views here.
