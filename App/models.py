from django.db import models

class tbl_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    role = models.CharField(max_length=25)

    class Meta:
        db_table = "tbl_login"

class tbl_zone(models.Model):
    zone_id = models.CharField(primary_key=True, max_length=25)
    zone = models.CharField(max_length=50)
    authority_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_zone"

class tbl_clinic(models.Model):
    clinic_id = models.CharField(primary_key=True, max_length=25)
    zone_id = models.ForeignKey(tbl_zone, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_clinic"

class tbl_volunteer(models.Model):
    volunteer_id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    zone_id = models.ForeignKey(tbl_zone, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(tbl_clinic,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_volunteer"

class tbl_patient_reg(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=25)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50)
    zone_id = models.ForeignKey(tbl_zone, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(tbl_clinic,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_patient_reg"

class tbl_help_request(models.Model):
    request_id = models.CharField(primary_key=True, max_length=25)
    patient_id  = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    request_dt = models.DateField()
    request_type = models.CharField(max_length=250)
    request = models.CharField(max_length=250)
    zone_id = models.ForeignKey(tbl_zone, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(tbl_clinic,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_help_request"

class tbl_volunteer_allot(models.Model):
    allot_id = models.CharField(primary_key=True, max_length=25)
    volunteer_id  = models.ForeignKey(tbl_volunteer,on_delete= models.CASCADE)
    allot_dt = models.DateField()
    request_id = models.ForeignKey(tbl_help_request,on_delete= models.CASCADE)
    patient_id = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    comment = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    updates = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_volunteer_allot"
    
class tbl_volunteer_allot1(models.Model):
    allot_id = models.CharField(primary_key=True, max_length=25)
    volunteer_id  = models.ForeignKey(tbl_volunteer,on_delete= models.CASCADE)
    allot_dt = models.DateField()
    request_id = models.ForeignKey(tbl_help_request,on_delete= models.CASCADE)
    patient_id = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    comment = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    updates = models.CharField(max_length=50)
    clinic_id = models.ForeignKey(tbl_clinic,on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_volunteer_allot1"

class tbl_idgen(models.Model):
    zid = models.IntegerField()
    cid = models.IntegerField()
    vid = models.IntegerField()
    pid = models.IntegerField()
    rid = models.IntegerField()
    aid = models.IntegerField()
    donid=models.IntegerField()
    comid=models.IntegerField()
    revid=models.IntegerField()
    upid=models.IntegerField()

    class Meta:
        db_table = "tbl_idgen"

class tbl_donation(models.Model):
    Donationid = models.CharField(primary_key=True, max_length=25)
    Donationname = models.CharField(max_length=50)
    Address = models.CharField(max_length=25)
    Phonenumber = models.CharField(max_length=25)
    Email = models.CharField(max_length=250)
    Itemdescription = models.CharField(max_length=50)
    Itemname = models.CharField(max_length=50)
    Donationdate = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_donation"

class tbl_complaint(models.Model):
    Complaintid = models.CharField(primary_key=True, max_length=25)
    patient_id  = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    Complaintdate = models.DateField()
    Complaint = models.CharField(max_length=250)

    class Meta:
        db_table = "tbl_complaint"

class tbl_review(models.Model):
    Reviewid = models.CharField(primary_key=True, max_length=25)
    patient_id  = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    Reviewdate = models.DateField()
    Review = models.CharField(max_length=250)

    class Meta:
        db_table = "tbl_review"

class tbl_update(models.Model):
    Updateid = models.CharField(primary_key=True, max_length=25)
    patient_id  = models.ForeignKey(tbl_patient_reg,on_delete= models.CASCADE)
    request_id  = models.ForeignKey(tbl_help_request,on_delete= models.CASCADE)
    Requirement = models.CharField(max_length=250)
    Updatestatus = models.CharField(max_length=250)

    class Meta:
        db_table = "tbl_update"
# Create your models here.
