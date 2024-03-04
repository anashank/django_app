from django.urls import path

from . import views

urlpatterns = [
path("",views.index,name="index"),
path("<int:id>",views.index2,name="index2"),
path("v1/",views.v1,name="v1"),
]