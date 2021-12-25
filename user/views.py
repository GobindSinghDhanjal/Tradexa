from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Post, User

# Create your views here.

def index(request):

    msg=""

    if(request.method =="POST"):
        userName=request.POST['username']
        password=request.POST['password']

        # print("username"+User.objects.get().username)

        try:
            data=User.objects.get(username=userName,password=password)
        except:
            data=None

        msg="Try again..."

        if(data):
            return redirect('post')
        else:
            return render(request,"index.html",{'msg': msg})
    else:
        print("else")
        return render(request,"index.html",{'msg': msg})

def register(request):
    if (request.method == "POST"):
        firstName=request.POST.get("firstName")
        lastName=request.POST.get("lastName")
        email=request.POST.get("email")
        password=request.POST.get("password")
        userName=request.POST.get("userName")

        Reg=User(first_name=firstName,
                     last_name=lastName,
                     email=email,
                     password=password,
                     username=userName)

        if User.objects.filter(email=email):
            msg="Email already exists"
            return render(request,'index.html',{'msg':msg})
        else:
            Reg.save()
            return redirect('index')
    else:
        return redirect('index.html')


def post(request):

    msg=""

    if(request.method =="POST"):
        user=request.POST.get('user')
        text=request.POST.get('text')
        created_at=request.POST.get('created_at')
        updated_at=request.POST.get('updated_at')
        userName=request.POST.get('userName')

        # print("username"+User.objects.get().username)

        try:
            data=User.objects.get(username=userName)
            
        except:
            data=None
            msg="Wrong Username"

        if(data):
            msg="Posted"
            p=Post(user=user,
                    text=text,
                    created_at=created_at,
                    updated_at=updated_at,
                    username=data)
            p.save()
            return render(request,'post.html',{'msg': msg})
        else:
            return render(request,'post.html',{'msg': msg})
    else:
        print("else")
        return render(request,"post.html")