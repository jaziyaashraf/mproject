from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('adm_view_rating/', views.adm_view_rating),
    path('adm_rgstr_regisrer/',views.adm_rgstr_regisrer),
    path('adm_rply_reply/', views.adm_rply_reply),
    path('adm_view_complaint/', views.adm_view_complaint),
    path('adm_view_employees/', views.adm_view_employees),

path('adm_view_feedback/', views.adm_view_feedback),
path('adm_view_furniture_shop/', views.adm_view_furniture_shop),
path('adm_View_rating_more/', views.adm_rating_more),
path('adm_view_registerd_users/', views.adm_view_registered_users),
path('adm_homepage/', views.adm_homepage),

]
