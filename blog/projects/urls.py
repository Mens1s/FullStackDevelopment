from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects),
    path('atmproject', views.atmproject,name="atmproject"),
    path('atmproject2', views.atmproject2,name='atmproject2')
]  