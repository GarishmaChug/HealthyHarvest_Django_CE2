from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_for_job, name='apply'),
    path('applications/', views.admin_applications_view, name='admin_applications'),
    path('applications/<int:pk>/<str:status>/', views.update_status, name='update_status'),
    path('',views.home,name="delivery_home"),
    path('logout/', views.logout_view, name='logout'),
    path('privacy/',views.privacy,name='privacy')
]
