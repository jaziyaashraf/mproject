from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    utype=models.CharField(max_length=50)


class customer(models.model):name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    image=models.FileField(max_length=200)
    house_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)






class employees(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    image=models.FileField(max_length=200)
    experience=models.CharField(max_length=50)
    house_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class rating(models.Model):
    rating=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50)
    date=models.DateField(max_length=50)
    review=models.CharField(max_length=50)
    CUSTOMER=models.ForeignKey(customer,on_delete=models.CASCADE)


class furnitureshop(models.Model):

    shop_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    city=models.CharField(max_length=50)


class complaint(models.Model):
    complaints=models.TextField(max_length=100)
    date=models.DateField(max_length=50)
    reply=models.TextField(max_length=50)
    status=models.CharField(max_length=50)
    CUSTOMER=models.ForeignKey(customer,on_delete=models.CASCADE)


class feedback(models.Model):
     feedbacks=models.CharField(max_length=100)
     CUSTOMER=models.ForeignKey(customer,on_delete=models.CASCADE)


class salary(models.Model):
    salary=models.CharField(max_length=50)
    EMPLOYEES=models.ForeignKey(employees, on_delete=models.CASCADE)

class previous_work(models.Model):
    worktitle=models.CharField(max_length=50)
    work_details=models.TextField(max_length=50)
    file=models.FileField(max_length=50)
    CUSTOMER = models.ForeignKey(customer, on_delete=models.CASCADE)


class plan(models.Model):
    plan_name=models.CharField(max_length=50)
    plan_details=models.TextField(max_length=100)
    file=models