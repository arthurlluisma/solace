from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="solace"),
    path("home", views.home, name="home"),
    path("login", views.register, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("searchapi", views.searchUser, name="searchapi"),
    path("sendfriendrequest", views.sendFriendRequest, name="sendfriendrequest"),
    path("createpet", views.createPet, name="createpet"),
]
