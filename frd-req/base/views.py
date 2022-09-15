from django.shortcuts import render,redirect
from .models import User,Post
from .forms import Userform
from django.contrib.auth import authenticate,login,logout
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


def post(request,no):
    post=Post.objects.get(id=no)
    context={'post':post}
    return render(request,'post.html',context)