import random

import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Dream_Growth_Architects_and_Interiors.models import login, employees, rating, customer, furnitureshop, \
    furniture_details, furniturecategory, plan, previous_work, design, complaint


def ab(request):
    return render(request,"admin_index.html")

def loginn(request):
    if request.method=="POST":
        user=request.POST['username']
        psw=request.POST['pass']
        lg=login.objects.filter(username=user,password=psw)
        if lg.exists():
            lg=lg[0]
            request.session['lid']=lg.id
            if lg.utype=="admin":
                return render(request,"Admin architect/homepage.html")
            elif lg.utype=="Architect":
                return render(request,"Architect/homepage.html")
            elif lg.utype=="furniture":
                return render(request,"furniture_shop/homepage.html")
            elif lg.utype=="Designer":
                return render(request,"Designer/homepage.html")
            else:
                return HttpResponse("Invalid user")
        else:
            return HttpResponse("Invalid details")

    return render(request,"login_temp.html")
    # return render(request,"Login.html")

def adm_view_rating(request):
    return render(request,"Admin architect/Rating.html")
def adm_rgstr_regisrer(request):
    return render(request, "Admin architect/Register_employees.html")


def adm_rgstr_regisrerpost(request):
    name=request.POST['name']
    gender=request.POST['radio']
    dob=request.POST['dob']
    email=request.POST['email']
    phone=request.POST['phone']
    experience=request.POST['experience']
    housename=request.POST['housename']
    district=request.POST['select2']
    pincode=request.POST['pincode']
    type=request.POST['type']


    image=request.FILES['image']
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    path='/media/'+image.name
    password=str(random.randint(1000,9999))
    lg=login()
    lg.username=email
    lg.password=password
    lg.utype=type
    lg.save()

    emp=employees()
    emp.name=name
    emp.gender=gender
    emp.dob=dob
    emp.email=email
    emp.phone=phone
    emp.experience=experience
    emp.house_name=housename
    emp.district=district
    emp.pincode=pincode
    emp.type=type
    emp.image=fs.url(filename)
    emp.LOGIN=lg
    emp.save()
    return render(request,"Admin architect/Register_employees.html")
def adm_employee_edit(request,pk):
    res=employees.objects.get(pk=pk)
    request.session['id']=pk
    return render (request,"Admin architect/edit_profile.html",{'data':res})

def adm_employee_edit_post(request):
    id=request.session['id']
    ename=request.POST['name']
    gender=request.POST['radio']
    edob=request.POST['dob']
    email=request.POST['email']
    phone=request.POST['phone']
    experience=request.POST['experience']
    housename=request.POST['house']
    district=request.POST['district']
    pincode=request.POST['pincode']
    res=employees.objects.get(id=id)
    res.name=ename
    res.gender=gender
    res.dob=edob
    res.email=email
    res.phone=phone
    res.experience=experience
    res.house_name=housename
    res.district=district
    res.pincode=pincode

    if 'image' in request.FILES:
        img=request.FILES['image']
        if img.name=='':
            pass
        else:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            res.image=fs.url(filename)

    res.save()
    return adm_view_employees(request)

def adm_employee_del(request,pk):
    print(pk)
    res=employees.objects.get(pk=pk)
    res.delete()
    return render(request,"Admin architect/homepage.html")

def adm_rply_reply(request):
    return render(request,"Admin architect/sent_reply.html")

def adm_view_complaint(request):
    res=complaint.objects.filter(status='pending')
    return render(request,"Admin architect/View_complaint.html",{'res':res})

def adm_view_employees(request):
    emp_obj=employees.objects.all()
    return render (request,"Admin architect/View_employees.html",{'data':emp_obj})

def adm_view_feedback(request):
    return render (request, "Admin architect/view_feedbacks.html")

def adm_view_furniture_shop(request):
    fur_obj = furnitureshop.objects.filter(status="pending")
    print('123')
    return render (request,"Admin architect/View_furniture_shop.html",{'data':fur_obj})

def adm_rating_more(request):
    return render (request,"Admin architect/View_rating_more.html")

def adm_view_registered_users(request):
    userall=customer.objects.all()
    return render(request,"Admin architect/view_registered_users.html",{'data':userall})

def adm_homepage(request):
    return render(request,"Admin architect/homepage.html")
def edit_profile_designer(request):
    lid = request.session['lid']
    res = employees.objects.get(LOGIN=lid)
    return render(request,"Designer/edit_profile.html",{'res':res})

def designer_edit_profile_post(request):
    id = request.session['lid']
    ename = request.POST['name']
    gender = request.POST['radio']
    edob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    experience = request.POST['experience']
    housename = request.POST['house']
    district = request.POST['district']
    pincode = request.POST['pincode']
    res = employees.objects.get(LOGIN=login.objects.get(id=id))


    if 'img' not in request.FILES:
        res.name = ename
        res.gender = gender
        res.dob = edob
        res.email = email
        res.phone = phone
        res.experience = experience
        res.house_name = housename
        res.district = district
        res.pincode = pincode

    else:
        img = request.FILES['img']
        if img.name == '':
            pass
        else:
            res.name = ename
            res.gender = gender
            res.dob = edob
            res.email = email
            res.phone = phone
            res.experience = experience
            res.house_name = housename
            res.district = district
            res.pincode = pincode
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            res.image = fs.url(filename)
            res.save()
    arc_obj= employees.objects.get(LOGIN=login.objects.get(id=id))
    return render(request, "Designer/view_desiner_profile.html", {'res': arc_obj})






def arc_edit_profile_post(request):
    id = request.session['lid']
    ename = request.POST['name']
    gender = request.POST['radio']
    edob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    experience = request.POST['experience']
    housename = request.POST['house']
    district = request.POST['district']
    place = request.POST['place']
    pincode = request.POST['pincode']
    res = employees.objects.get(LOGIN=login.objects.get(id=id))
    res.name = ename
    res.gender = gender
    res.dob = edob
    res.email = email
    res.phone = phone
    res.experience = experience
    res.house_name = housename
    res.district = district
    res.place = place
    res.pincode = pincode

    if 'image' in request.FILES:
        img = request.FILES['image']
        if img.name == '':
            pass
        else:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            res.image = fs.url(filename)

    res.save()
    arc_obj= employees.objects.get(LOGIN=login.objects.get(id=id))
    return render(request, "Architect/view_profile.html", {'data': arc_obj})


def archi_change_password(request):
    if request.method == "POST":
        currentpassword = request.POST["currentpassword"]
        newpassword = request.POST["newpassword"]
        confirmapssword = request.POST["confirmpassword"]

        lid = request.session["lid"]

        loginobj = login.objects.filter(pk=lid)

        if loginobj.exists():
            loginobj = login.objects.get(pk=lid)
            if currentpassword == loginobj.password:
                if newpassword == confirmapssword:
                    loginobj.password = newpassword
                    loginobj.save()
                    return HttpResponse("<script>alert('Password Chenged Successfully');window.location='/myapp/'</script>")
                else:
                    return HttpResponse("<script>alert('Password Mismatch.Try again');window.location='/myapp/archi_change_password/'</script>")

            else:
                return HttpResponse("<script>alert('Enter valid password.Try again');window.location='/myapp/archi_change_password/'</script>")
        else:
            return HttpResponse("<script>alert('Enter valid password.Try again');window.location='/myapp/'</script>")

    return render(request, "Architect/change password.html")


def furnitureshop_reg(request):

    if request.method=="POST":

        furnitureshopobj=furnitureshop()
        furnitureshopobj.shop_name=request.POST["shop_name"]
        furnitureshopobj.ownername=request.POST["ownername"]
        furnitureshopobj.phone=request.POST["phone"]
        furnitureshopobj.email=request.POST["email"]
        furnitureshopobj.district=request.POST["district"]
        furnitureshopobj.state=request.POST["state"]
        furnitureshopobj.city=request.POST["city"]
        furnitureshopobj.latitide=request.POST["latitude"]
        furnitureshopobj.longitude=request.POST["longitude"]

        furnitureshopobj.status="pending"


        loginobj=login()
        loginobj.username=request.POST["email"]
        loginobj.password=request.POST["password"]
        # loginobj.utype="furniture"
        loginobj.utype = "pending"
        loginobj.save()

        furnitureshopobj.LOGIN= loginobj

        furnitureshopobj.save()

        return HttpResponse("<script>alert('Account created Successfully');window.location='/myapp/'</script>")

    return render(request,"furniture_shop/furniture shop registration.html")


def furnitureshop_view_profile(request):
    lid=request.session['lid']
    log_obj=login.objects.get(id=lid)
    fur_obj=furnitureshop.objects.get(LOGIN=log_obj)
    if request.method=='POST':
        return render(request,"furniture_shop/Edit furniture shop.html",{'data':fur_obj})
    return render(request,"furniture_shop/viewprofile.html",{'data':fur_obj})


def furnitureshop_edit(request,pk):
    request.session['id']=pk
    res=furnitureshop.objects.get(id=pk)
    return render(request,"furniture_shop/Edit furniture shop.html",{'res':res})
def furnitureshop_edit_post(request):
    id=request.session['lid']
    print(id)
    shname=request.POST['shop_name']
    ownername=request.POST['ownername']
    state= request.POST['state']
    district= request.POST['district']
    city= request.POST['city']
    phone = request.POST['phone']
    email=request.POST['email']
    latitude= request.POST['latitude']
    longitude = request.POST['longitude']
    res=furnitureshop.objects.get(LOGIN=id)
    print(res)
    print("123")

    res.shop_name=shname
    res.ownername=ownername
    res.state=state
    res.district=district
    res.city=city
    res.phone=phone
    res.email=email
    res.latitude=latitude
    res.longitude=longitude

    res.save()
    fur_obj=furnitureshop.objects.get(LOGIN=login.objects.get(id=id))
    return render(request, "furniture_shop/viewprofile.html", {'data':fur_obj})


def furniture_category(request):

    if request.method=="POST":
        categoryname= request.POST["textfield"]
        lid=request.session["lid"]

        loginobj=login.objects.get(pk=lid)

        fobj=furniturecategory()
        fobj.catname=categoryname
        fobj.FLOGIN=loginobj
        fobj.save()

    return render(request,"furniture_shop/Add category.html")

def furniture_category_view(request):


    allfurniturecategory=furniturecategory.objects.all()

    return render(request, "furniture_shop/viewfurniturecategory.html",{'data': allfurniturecategory})


def furnitureshopprofile(request):
    lid=request.session["lid"]
    res=furnitureshop.objects.get(LOGIN= login.objects.get(pk=lid))
    return  render(request,"furniture_shop/viewprofile.html",{'data': res})





def furniturecategoryedit(request,id):
    categoryname = request.POST["textfield"]
    categoryobj=furniturecategory.objects.get(pk=id)
    categoryobj.catname=categoryname
    categoryobj.save()


    return  redirect('')


def furniture_category_del(request,pk):
    categoryobj=furniturecategory.objects.get(pk=pk)
    categoryobj.delete()
    return redirect("myapp:furniture_category_view")




def furnituredetails(request):
    res=furniturecategory.objects.all()
    lid=request.session["lid"]
    loginobj=login.objects.get(pk=lid)


    if request.method=='POST':
        fname=request.POST['nm']
        print(fname)
        categor=request.POST['select2']
        print(categor)
        catobj=furniturecategory.objects.get(pk=categor)
        print(catobj.id)
        descr=request.POST['textfield5']
        image=request.FILES["ff"]
        print(image)
        woodtype=request.POST['select']
        amount=request.POST['textfield4']
        fs = FileSystemStorage()
        f = fs.save(image.name, image)
        res1=furniture_details(furniturename=fname,category_id=catobj.id,file= fs.url(f),wood_type=woodtype,Amount=amount,LOGIN_id=loginobj.id,description=descr)
        res1.save()
    return render(request,"furniture_shop/furniture details.html",{'res':res})



def furniture_details_view(request):
    lid=request.session["lid"]
    loginobj=login.objects.get(pk=lid)
    res=furniture_details.objects.filter(LOGIN_id=loginobj.id)

    return render(request,"furniture_shop/VIEW FURNITURE DETAILS.html",{'res':res})
def furniture_details_edit(request,id):
    request.session['id']=id
    res1=furniturecategory.objects.all()

    res=furniture_details.objects.get(id=id)
    return render(request,"furniture_shop/edit furniture details.html",{'data':res,'res1':res1})
def furniture_details__post(request):
    id = request.session['id']
    print(id)
    fname = request.POST['furniturename']
    print(fname)

    print(id)

    category = request.POST['category']
    print(category)
    amount= request.POST['amount']
    print(amount)
    wood=request.POST['woodtype']
    print(wood)
    description= request.POST['description']
    print(description)
    res=furniture_details.objects.get(pk=id)
    print(res)
    if request.method=='POST':

        if 'ff' not in request.FILES:
            print("hii")
            res.furniturename = fname
            res.category_id = category
            res.wood_type = wood
            res.description = description
            res.Amount = amount
            res.save()
        else:
            image=request.FILES["ff"]
            if image.name=='':
                print("hii")
                res.furniturename = fname
                res.category_id = category
                res.wood_type = wood
                res.description = description
                res.Amount = amount
                res.save()
            else:
                print("123")
                fs = FileSystemStorage()
                f = fs.save(image.name, image)
                res.furniturename = fname
                res.category_id = category
                res.wood_type = wood
                res.description = description
                res.Amount = amount
                res.file=fs.url(f)
                res.save()
    return redirect("/myapp/furniture_details_view/")

def furniture_viewdetails_delete(request,id):
    res=furniture_details.objects.get(pk=id)
    res.delete()
    return redirect("/myapp/furniture_details_view/")

def furniture_viewdetails_search(request):
    lid=request.session['lid']
    fname=request.POST['fn']
    res=furniture_details.objects.filter(LOGIN_id=lid,furniturename=fname)
    return render(request,"furniture_shop/VIEW FURNITURE DETAILS.html",{'res':res})

def admin_view_users(request):
    res=customer.objects.all()
    return render(request,"Admin architect/view_users.html",{'res':res})


def plan_details(request):
    return render(request,"Architect/plan_details")
def arc_upload_prework(request):
    return render(request,"Architect/Upload_previous_work.html")
def aprv_furntrshop(request):
    fur_obj=furnitureshop.objects.filter(LOGIN__utype='pending')
    return render(request,"Admin architect/approve or reject furniture shop.html",{'data':fur_obj})
def view_approved_furniture_shop(request):
    fur_obj=furnitureshop.objects.filter(LOGIN__utype='furniture')
    return render(request,"Admin architect/view_approved_furniture_shop.html",{'data':fur_obj})

def aprv_furntrshop_stat(request,id,status):
    fur_obj=furnitureshop.objects.get(id=id)
    lg=fur_obj.LOGIN_id
    log=login.objects.get(id=lg)
    log.utype=status
    log.save()
    return HttpResponse("Success")



def samples(request):
    return render(request,'furnituresignup.html')


def arc_addplan(request):

    if request.method=="POST":

        planobj=plan()
        planobj.plan_name=request.POST["planname"]
        planobj.squarefeet=request.POST["totalsquarefeet"]

        if 'fileField' in request.FILES:
            img = request.FILES['fileField']
            if img.name == '':
                pass
            else:
                image = request.FILES['fileField']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                planobj.file = fs.url(filename)

        planobj.date=datetime.datetime.now()
        planobj.amount=request.POST["totalbudget"]
        planobj.description=request.POST["description"]


        planobj.ARCHITECT= employees.objects.get(LOGIN=login.objects.get(pk=request.session["lid"]))

        planobj.save()

        pass
    return render(request,'Architect/Plan_details.html')

def arc_editplan(request,id):
    print("jjjj")
    planobj=plan.objects.get(pk=id)
    print(planobj)
    request.session["planid"]=str(id)
    print("oppppp")
    return render(request,'Architect/editplan.html',{'data': planobj})


def arc_deleteplan(request, id):
    planobj = plan.objects.get(pk=id)
    planobj.delete()
    return HttpResponse("<script>alert('Plan deleted successfully');window.location='/myapp/arc_viewplan/'</script>")

def arc_view_profile(request):
    lid=request.session['lid']
    res=employees.objects.get(LOGIN=lid)
    return render(request,"Architect/view_profile.html",{'data':res})
def arc_edit_plan_post(request):

    if request.method=="POST":
        print("entr22")

        planid=request.session["planid"]
        print("plnid=",planid)
        planobj=plan.objects.get(pk=planid)
        print("pln obj")
        print(planobj)
        planobj.plan_name=request.POST["planname"]
        planobj.squarefeet=request.POST["totalsquarefeet"]
        print("next")

        if 'fileField' in request.FILES:
            print("img22")
            img = request.FILES['fileField']
            if img.name == '':
                print("mmmss")
                pass
            else:
                print("entr")
                image = request.FILES['fileField']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                planobj.file = fs.url(filename)

        planobj.date=datetime.datetime.now()
        planobj.amount=request.POST["totalbudget"]
        planobj.description=request.POST["description"]



        planobj.save()

        pass
    return redirect("/myapp/arc_viewplan/")




def arc_viewplan(request):

    allplans= plan.objects.filter(ARCHITECT=employees.objects.get(LOGIN=login.objects.get(pk=request.session["lid"])))
    return  render(request,'Architect/view_plan.html',{'data': allplans})


def arc_changepassword(request):
    if request.method=="POST":
        currentpassword=request.POST["currentpassword"]
        newpassword=request.POST["newpassword"]
        confirmapssword=request.POST["confirmpassword"]

        lid=request.session["lid"]

        loginobj= login.objects.filter(pk=lid)

        if loginobj.exists():
            loginobj=login.objects.get(pk=lid)
            loginobj.password=newpassword
            loginobj.save()

            return HttpResponse("<script>alert('Password Chenged Successfully');window.location='/myapp/'</script>")

        return HttpResponse("<script>alert('Password Missmatched.Try again');window.location='/myapp/'</script>")
    return render(request,"Architect/change password.html")

def designer_view_profile(request):
    lid=request.session['lid']
    res=employees.objects.get(LOGIN_id=lid)
    return render(request,"Designer/view_desiner_profile.html",{'res':res})

def designer_changepassword(request):
    if request.method=="POST":
        currentpassword=request.POST["currentpassword"]
        newpassword=request.POST["newpassword"]
        confirmapssword=request.POST["confirmpassword"]

        lid=request.session["lid"]

        loginobj= login.objects.filter(pk=lid)


        if loginobj.exists():
            loginobj = login.objects.get(pk=lid)
            if currentpassword==loginobj.password:
                if newpassword==confirmapssword:
                    loginobj.password = newpassword
                    loginobj.save()
                    return HttpResponse("<script>alert('Password Chenged Successfully');window.location='/myapp/'</script>")
                else:
                    return HttpResponse("<script>alert('Password Mismatch.Try again');window.location='/myapp/designer_change_password/'</script>")

            else:
                return HttpResponse("<script>alert('Enter valid password.Try again');window.location='/myapp/designer_change_password/'</script>")
        else:
            return HttpResponse("<script>alert('Enter valid password.Try again');window.location='/myapp/'</script>")

    return render(request,"Designer/change password.html")

def designer_manage_works(request):
    return render(request,"Designer/Upload_previous_work.html")

def designer_manage_workspost(request):
    lid=request.session['lid']

    empobj=employees.objects.get(LOGIN=login.objects.get(pk=lid))

    title=request.POST['textfield2']
    details=request.POST['textfield']
    photo=request.FILES['fileField']
    fs=FileSystemStorage()
    filename = fs.save(photo.name, photo)
    path = '/media/' + photo.name

    if request.method=='POST':
        res=previous_work(worktitle=title,work_details=details,file=fs.url(filename),EMPLOYEE=empobj)
        res.save()
    return render(request, "Designer/Upload_previous_work.html")

def edit_previous_work(request,id):
    request.session['wid']=id
    res=previous_work.objects.get(pk=id)
    return render(request,"Designer/edit_previous_work.html",{'res':res})

def edit_previous_workpost(request):
    id=request.session['wid']



    title=request.POST['textfield2']
    details=request.POST['textfield']

    fs=FileSystemStorage()


    if request.method=='POST':
        res = previous_work.objects.get(pk=id)
        if 'fileField' not in request.FILES:

            res.worktitle=title
            res.work_details=details
            res.save()
        else:
            photo = request.FILES['fileField']
            if photo.name=='':
                res.worktitle = title
                res.work_details = details
                res.save()
            else:
                filename = fs.save(photo.name, photo)
                path = '/media/' + photo.name
                res.worktitle = title
                res.work_details = details
                res.file=fs.url(filename)
                res.save()
    return redirect("/myapp/designer_view_prevoius_works/")

def delete_previous_work(request,id):
    res = previous_work.objects.get(pk=id)
    res.delete()

    return redirect("/myapp/designer_view_prevoius_works/")

def designer_view_prevoius_works(request):
    lid=request.session['lid']
    empobj = employees.objects.get(LOGIN=login.objects.get(pk=lid))
    res=previous_work.objects.filter(EMPLOYEE=empobj)
    return render(request,"Designer/view_uploaded_previous_work.html",{'res':res})
def architect_manage_works(request):
    return render(request,"Architect/Upload_previous_work.html")

def architect_manage_workspost(request):
    lid = request.session['lid']

    empobj = employees.objects.get(LOGIN=login.objects.get(pk=lid))

    title = request.POST['textfield2']
    details = request.POST['textfield']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    path = '/media/' + photo.name

    if request.method == 'POST':
        res = previous_work(worktitle=title, work_details=details, file=fs.url(filename), EMPLOYEE=empobj)
        res.save()
    return render(request, "Architect/Upload_previous_work.html")

def architect_view_prevoius_works(request):
    lid = request.session['lid']
    empobj = employees.objects.get(LOGIN=login.objects.get(pk=lid))
    res = previous_work.objects.filter(EMPLOYEE=empobj)
    return render(request, "Architect/view_uploaded_previous_work.html", {'res': res})

def add_design(request):
    return render(request, "Designer/add_design.html")
def add_designpost(request):
    if request.method == "POST":

        planobj = design()
        planobj.design_name = request.POST["planname"]

        if 'fileField' in request.FILES:
            img = request.FILES['fileField']
            if img.name == '':
                pass
            else:
                image = request.FILES['fileField']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                planobj.file = fs.url(filename)

        planobj.date = datetime.datetime.now()
        planobj.amount = request.POST["totalbudget"]
        planobj.description = request.POST["description"]

        planobj.DESIGNER = employees.objects.get(LOGIN=login.objects.get(pk=request.session["lid"]))

        planobj.save()

        pass
    return render(request, 'Designer/add_design.html')

def view_design(request):
    lid=request.session['lid']
    empobj=employees.objects.get(LOGIN=login.objects.get(pk=lid))
    res=design.objects.filter(DESIGNER=empobj)
    return render(request,"Designer/view_designs.html",{'res':res})

def edit_design(request,id):
    request.session['did']=id
    res=design.objects.get(pk=id)
    return render(request,"Designer/edit_design.html",{'res':res})
def edit_designpost(request):
    if request.method=="POST":
        print("entr22")

        planid=request.session["did"]
        print("plnid=",planid)
        planobj=design.objects.get(pk=planid)
        print("pln obj")
        print(planobj)
        planobj.design_name=request.POST["planname"]
        print("next")

        if 'fileField' in request.FILES:
            print("img22")
            img = request.FILES['fileField']
            if img.name == '':
                print("mmmss")
                pass
            else:
                print("entr")
                image = request.FILES['fileField']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                planobj.file = fs.url(filename)

        planobj.date=datetime.datetime.now()
        planobj.amount=request.POST["totalbudget"]
        planobj.description=request.POST["description"]



        planobj.save()

        pass
    return redirect("/myapp/view_design/")

def delete_design(request, id):
    res = design.objects.get(pk=id)
    res.delete()
    return redirect("/myapp/view_design/")

def arc_edit_previous_work(request, id):
    request.session['wid'] = id
    res = previous_work.objects.get(pk=id)
    return render(request, "Architect/edit_previous_work.html", {'res': res})

def arc_edit_previous_workpost(request):
    id = request.session['wid']

    title = request.POST['textfield2']
    details = request.POST['textfield']

    fs = FileSystemStorage()

    if request.method == 'POST':
        res = previous_work.objects.get(pk=id)
        if 'fileField' not in request.FILES:

            res.worktitle = title
            res.work_details = details
            res.save()
        else:
            photo = request.FILES['fileField']
            if photo.name == '':
                res.worktitle = title
                res.work_details = details
                res.save()
            else:
                filename = fs.save(photo.name, photo)
                path = '/media/' + photo.name
                res.worktitle = title
                res.work_details = details
                res.file = fs.url(filename)
                res.save()
    return redirect("/myapp/architect_view_prevoius_works/")

def arc_delete_previous_work(request, id):
    res = previous_work.objects.get(pk=id)
    res.delete()

    return redirect("/myapp/architect_view_prevoius_works/")


    #
def and_login(request):
    if request.method=="POST":
        user=request.POST['username']
        psw=request.POST['password']
        lg=login.objects.filter(username=user,password=psw)
        if lg.exists():
            lg=lg[0]
            ty=lg.utype
            return JsonResponse({'status':"ok",'logid':lg.pk,'type':ty})
        else:
            return JsonResponse({'status':'no'})

def and_Reg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    email=request.POST['email']
    phone=request.POST['phone']
    image=request.FILES['img']
    house_name=request.POST['house_name']
    district=request.POST['district']
    pincode=request.POST['pin']
    city=request.POST['city']
    place=request.POST['place']
    passwor=request.POST['password']
    if request.method=='POST':
        fs=FileSystemStorage()
        filename = fs.save(image.name, image)
        path = '/media/' + image.name
        res=login(username=email,password=passwor,utype='user')
        res.save()
        res1=customer(name=name,gender=gender,dob=dob,email=email,phone=phone,image=fs.url(filename),house_name=house_name,district=district,pincode=pincode,city=city,place=place,LOGIN=res)
        res1.save()
        return JsonResponse({'status': 'ok'})


def and_view_profile(request):
    if request.method=="POST":
        lid=request.POST['lid']
        print(lid)
        res=customer.objects.filter(LOGIN=login.objects.get(pk=lid))
        if res.exists():
            res = customer.objects.get(LOGIN=login.objects.get(pk=lid))
            return JsonResponse({'status':'ok','name':res.name,'gender':res.gender,'dob':res.dob,'email':res.email,'phone':res.phone,'image':res.image,'house_name':res.house_name,'district':res.district,'pincode':res.pincode,'city':res.city,'place':res.place})
        else:
            return JsonResponse({'status': 'no'})


def and_change_password(request):
    if request.method == "POST":
        # currentpassword = request.POST["currentpassword"]
        newpassword = request.POST["password"]
        # confirmapssword = request.POST["confirmpassword"]
        lid = request.POST["lid"]

        loginobj = login.objects.filter(pk=lid)

        if loginobj.exists():
            loginobj = login.objects.get(pk=lid)
            if request.method=='POST':
                loginobj.password = newpassword
                loginobj.save()
                return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status':'no'})


def edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    email = request.POST['email']
    phone = request.POST['phone']
    house_name = request.POST['house_name']
    district = request.POST['district']
    pincode = request.POST['pin']
    city = request.POST['city']
    place = request.POST['place']
    res=customer.objects.filter(LOGIN=login.objects.get(pk=lid))
    if res.exists():
        res = customer.objects.get(LOGIN=login.objects.get(pk=lid))
        if request.method == 'POST':
            if 'img' not in request.FILES:
                res.name=name
                res.gender=gender
                res.dob=dob
                res.email=email
                res.place=place
                res.pincode=pincode
                res.city=city
                res.district=district
                res.house_name=house_name
                res.phone=phone
                res.save()
                return JsonResponse({'status': 'ok'})
            else:
                image = request.FILES['img']
                if image.name=='':
                    res.name = name
                    res.gender = gender
                    res.dob = dob
                    res.email = email
                    res.place = place
                    res.pincode = pincode
                    res.city = city
                    res.district = district
                    res.house_name = house_name
                    res.phone = phone
                    res.save()
                    return JsonResponse({'status': 'ok'})
                else:
                    fs = FileSystemStorage()
                    filename = fs.save(image.name, image)
                    path = '/media/' + image.name
                    res.image = fs.url(filename)
                    res.name = name
                    res.gender = gender
                    res.dob = dob
                    res.email = email
                    res.place = place
                    res.pincode = pincode
                    res.city = city
                    res.district = district
                    res.house_name = house_name
                    res.phone = phone
                    res.save()
                    return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})





