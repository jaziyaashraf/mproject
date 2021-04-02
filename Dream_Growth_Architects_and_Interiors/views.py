from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"Login.html")

def adm_view_rating(request):
    return render(request,"Admin architect/Rating.html")

def adm_rgstr_regisrer(request):
    return render(request,"Admin architect/Register_employees.html.html")

def adm_rply_reply(request):
    return render(request,"Admin architect/sent_reply.html")

def adm_view_complaint(request):
    return render(request,"Admin architect/View_complaint.html")

def adm_view_employees(request):
    return render (request,"Admin architect/view_feedbacks.html")

def adm_view_feedback(request):
    return render (request, "Admin architect/view_feedbacks.html")

def adm_view_furniture_shop(request):
    return render (request,"Admin architect/View_furniture_shop.html")

def adm_rating_more(request):
    return render (request,"Admin architect/View_rating_more.html")

def adm_view_registered_users(request):
    return render(request,"Admin architect/view_registered_users.html")

def adm_homepage(request):
    return render(request,"Admin architect/homepage.html")
