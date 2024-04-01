from django.urls import path

from . import views

urlpatterns = [
path("",views.v2,name="v2"),
path("v3/",views.home,name="home"),
path("<int:id>",views.index2,name="index2"),
path("v1/",views.v1,name="v1")
]