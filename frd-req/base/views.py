from django.shortcuts import render,redirect
from .models import User,Post,Friend_request
from .forms import Userform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    form=Userform()
    post=Post.objects.all()
    context={'forms':form,'posts':post}
    if request.method =="POST":
            
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            context={'forms':form,'error':"wrong",'posts':post}
            return render(request,'home.html',context)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context={'forms':form,'error':"wrong",'posts':post}
            return render(request,'home.html',context)
    return render(request,'home.html',context)


def logoutuser(request):
    logout(request)
    return redirect('home')


def send_request(request,no):
    from_user=request.user
    to_user=User.objects.get(id=no)
    fredreq=Friend_request.objects.get_or_create(from_user=from_user,to_user=to_user)
    return redirect('home')

def accept_request(request,no):
    frd_req=Friend_request.objects.get(id=no)
    user1=request.user
    user2=frd_req.from_user
    user1.friendreq.add(user2)
    user2.friendreq.add(user1)
    frd_req.delete()
    return redirect('home')

@login_required(login_url="home")
def friendlist(request):
    frd_req=Friend_request.objects.filter(to_user=request.user)
    context={'frdreq':frd_req,}
    return render(request,'frd_req.html',context)

def post(request,no):
    post=Post.objects.get(id=no)
    context={'post':post}
    return render(request,'post.html',context)