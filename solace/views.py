import re

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.


def landing(request):
    return render(request, "solace/landing.html", {"user": request.user})


def register(request):
    if request.method == "POST":
        method = request.POST["method"]
        username = request.POST["username"]
        password = request.POST["password"]
        username_regex = re.compile(r"^\S+$")
        if method == "r":
            if not username_regex.match(username):
                return render(
                    request,
                    "solace/login.html",
                    {
                        "user": request.user,
                        "error": "Invalid login details",
                        "landing": True,
                    },
                )
            else:
                try:
                    checkuser = User.objects.get(username=username.lower())
                    return render(
                        request,
                        "solace/login.html",
                        {
                            "user": request.user,
                            "error": "Username already exists",
                            "landing": "True",
                        },
                    )
                except User.DoesNotExist:
                    user = User.objects.create_user(username, password)
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse("login"))
        else:
            if not username_regex.match(username):
                return render(
                    request,
                    "solace/login.html",
                    {
                        "user": request.user,
                        "error": "Invalid login details",
                        "landing": True,
                    },
                )
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    return render(
                        request,
                        "solace/login.html",
                        {
                            "user": request.user,
                            "error": "Invalid Password",
                            "landing": "True",
                        },
                    )
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "solace/login.html", {"landing": "True"})


def home(request):
    if request.user.is_authenticated:
        if Pet.objects.filter(owner=request.user).exists():
            return render(request, "solace/index.html", {
                "friends": request.user.friends.all(),
                "pet": Pet.objects.get(owner=request.user)
            })
        else:
            return render(request, "solace/index.html", {
                "friends": request.user.friends.all(),
                "noPet": "true"
            })

    else:
        return HttpResponseRedirect(reverse("solace"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("solace"))


@csrf_exempt
def searchUser(request):
    if request.method == "POST":
        print("test")
        try:
            checkuser = User.objects.get(username=request.POST["username"])
            if checkuser.friends.filter(id=request.user.id).exists():
                return JsonResponse({
                    "found": "false",
                    "message": "Already friends with this user."
                })
            else:
                request.user.addFriend(checkuser)
                return JsonResponse(
                    {
                        "found": "true",
                        "user": {
                            "username": checkuser.username,
                            "status": checkuser.status,
                        },
                    }
                )
        except User.DoesNotExist:
            return JsonResponse({
                "found": "false",
                "message": "User does not exist."
            })

@csrf_exempt
def sendFriendRequest(request):
    user = User.objects.get(username=request.POST["username"])
    try:
        user.send_friend_request(request.user)
        return JsonResponse({
            "success": "true"
        })
    except:
        return JsonResponse({
            "success": "false"
        })

@csrf_exempt
def acceptFriendRequest(request):
    user = User.objects.get(username=request.POST["username"])
    try:
        request.user.friends.remove(user)
        request.user.addFriend(user)
        return JsonResponse({
            "success": "true"
        })
    except:
        return JsonResponse({
            "success": "false"
        })

@csrf_exempt
def createPet(request):
    if request.method == 'POST':
        owner = request.user
        name = request.POST["name"]
        sprite = request.POST["sprite"]
        Pet.objects.create(owner=owner, name=name, sprite=sprite)
        return JsonResponse({
            "success": "false"
        })