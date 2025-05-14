from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
    path('save-schedule/', views.save_schedule, name='save_schedule'),
] 