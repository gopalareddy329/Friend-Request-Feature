from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('post/<str:no>',views.post,name="post")
]