from django.urls import path
from . import views

urlpatterns=[
    path("",views.additem,name="todo"),
    path("del/<int:item_id>",views.removeitem,name="del")
]