from django.urls import path
from . import views
app_name="myapp"

urlpatterns = [
    path('', views.loginn),
    path('adm_view_rating/', views.adm_view_rating),
    path('adm_rgstr_regisrer/',views.adm_rgstr_regisrer),
    path('adm_rgstr_regisrerpost/',views.adm_rgstr_regisrerpost),
    path('adm_rply_reply/', views.adm_rply_reply),
    path('adm_view_complaint/', views.adm_view_complaint),
    path('adm_view_employees/', views.adm_view_employees),
path('adm_employee_edit/<str:pk>', views.adm_employee_edit),
    path('adm_employee_edit_post', views.adm_employee_edit_post),
    path('adm_employee_del/<str:pk>',views.adm_employee_del),
    path('adm_view_feedback/', views.adm_view_feedback),
    path('adm_view_furniture_shop/', views.adm_view_furniture_shop),
    path('adm_View_rating_more/', views.adm_rating_more),
    path('adm_view_registerd_users/', views.adm_view_registered_users),
    path('adm_homepage/', views.adm_homepage),
    path('designer_view_prevoius_works/', views.designer_view_prevoius_works),
    path('architect_manage_works/',views.architect_manage_works),
    path('architect_manage_workspost/', views.architect_manage_workspost),
    path('add_design/',views.add_design),
    path('add_designpost/', views.add_designpost),
    path('view_design/', views.view_design),
    path('edit_design/<int:id>',views.edit_design),
    path('edit_designpost/', views.edit_designpost),
    path('delete_design/<int:id>', views.delete_design),
    path('edit_previous_work/<int:id>',views.edit_previous_work),
    path('edit_previous_workpost/',views.edit_previous_workpost),
    path('delete_previous_work/<int:id>',views.delete_previous_work),

    path('arc_edit_previous_work/<int:id>', views.arc_edit_previous_work),
    path('arc_edit_previous_workpost/', views.arc_edit_previous_workpost),
    path('arc_delete_previous_work/<int:id>', views.arc_delete_previous_work),

    path('architect_view_prevoius_works/',views.architect_view_prevoius_works),

    path('archi_change_password/', views.archi_change_password),
    path('furniture_category_del/<str:pk>',views.furniture_category_del),
    path('ab/', views.ab),
    path('view_approved_furniture_shop/',views.view_approved_furniture_shop),


    path('arc_view_profile/',views.arc_view_profile),
   path('arc_edit_profile_post/',views.arc_edit_profile_post),
   path('furnitureshop_reg/',views.furnitureshop_reg),


path('furnitureshop_edit/<str:pk>',views.furnitureshop_edit),
path('furnitureshop_view_profile/',views.furnitureshop_view_profile),
path('furnitureshop_edit_post/',views.furnitureshop_edit_post),
path( 'furniture_category/', views.furniture_category),
path( 'furniture_category_view/', views.furniture_category_view,name="furniture_category_view"),
path( 'furnitureshopprofile/', views.furnitureshopprofile,name="furnitureshopprofile"),

path('furniture_details/',views.furnituredetails),
path('furniture_details_post/',views.furnituredetails),
path('furniture_details_view/',views.furniture_details_view),
path('furniture_viewdetails_edit/<int:id>',views.furniture_details_edit),
path('furniture_details__post/',views.furniture_details__post),
path('furniture_viewdetails_delete/<int:id>',views.furniture_viewdetails_delete),
path('furniture_viewdetails_search/',views.furniture_viewdetails_search),
path('admin_view_users/',views.admin_view_users),
path('designer_view_profile/',views.designer_view_profile),
path('designer_change_password/',views.designer_changepassword),
path('designer_manage_works/',views.designer_manage_works),
path('designer_manage_workspost/',views.designer_manage_workspost),

path('furnituresignup/',views.samples),


path('furniture_details_edit/',views.furniture_details_edit),

path('plan_details/',views.plan_details),

path('arc_upload_prework/',views.arc_upload_prework),
path('aprv_furntrshop/',views.aprv_furntrshop),
path('aprv_furntrshop_stat/<str:id>/<str:status>',views.aprv_furntrshop_stat),


path('arc_changepassword/',views.arc_changepassword),
path('arc_addplan/',views.arc_addplan),
path('arc_viewplan/',views.arc_viewplan),

path('arc_viewplan_edit/<str:id>',views.arc_editplan),

path('arc_edit_plan_post',views.arc_edit_plan_post),

path('arc_viewplan_delete/<str:id>',views.arc_deleteplan),
path('and_login/',views.and_login),
path('and_Reg/',views.and_Reg),
path('and_view_profile/',views.and_view_profile),
path('and_change_password/',views.and_change_password),
path('edit_profile/',views.edit_profile),
path('edit_profile_designer/',views.edit_profile_designer),
path('designer_edit_profile_post/',views.designer_edit_profile_post),

    ]



