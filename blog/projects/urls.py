from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects),
    path('atmproject', views.atmproject,name="atmproject"),
    path('atmprojectregister', views.atmprojectregister, name="atmprojectregister"),
    path('atmprojectuser',views.atmprojectuser, name="atmprojectuser")
]  