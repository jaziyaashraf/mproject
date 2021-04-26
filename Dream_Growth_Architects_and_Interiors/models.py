from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    utype=models.CharField(max_length=50)


class furniturecategory(models.Model):
    catname=models.CharField(max_length=100)
    FLOGIN=models.ForeignKey(login,on_delete=models.CASCADE)


class customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    house_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
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
    EMPLOYEE=models.ForeignKey(employees,on_delete=models.CASCADE,default="1")


class furnitureshop(models.Model):

    shop_name=models.CharField(max_length=50)
    ownername=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    latitide=models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
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
    EMPLOYEE = models.ForeignKey(employees, on_delete=models.CASCADE)


class plan(models.Model):
    plan_name=models.CharField(max_length=50,default="")
    squarefeet=models.TextField(max_length=100,default="")
    file=models.CharField(max_length=500,default="")
    date=models.DateField(max_length=50,default="2020-01-01")
    amount=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=500,default="")
    ARCHITECT= models.ForeignKey(employees,on_delete=models.CASCADE,default=1)

class design(models.Model):
    design_name=models.CharField(max_length=50,default="")
    file=models.CharField(max_length=500,default="")
    date=models.DateField(max_length=50,default="2020-01-01")
    amount=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=500,default="")
    DESIGNER= models.ForeignKey(employees,on_delete=models.CASCADE,default=1)

class furniture_details(models.Model):
    furniturename=models.CharField(max_length=50)
    category=models.ForeignKey(furniturecategory, on_delete=models.CASCADE)
    Amount=models.CharField(max_length=50)
    file=models.FileField(max_length=100)
    description=models.CharField(max_length=50)
    wood_type=models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)