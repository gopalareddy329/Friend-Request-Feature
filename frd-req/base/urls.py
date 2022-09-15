from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('post/<str:no>',views.post,name="post"),
    path('frdreq',views.friendlist,name="frdreq"),
    path('sendreq/<str:no>',views.send_request,name="sendreq"),
    path('accpetreq/<str:no>',views.accept_request,name="accpetreq"),
]