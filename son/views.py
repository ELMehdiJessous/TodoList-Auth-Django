from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    task = Task.objects.filter(user = request.user)
    taskform = TaskForm()
    if request.method == "POST":
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            y = taskform.save(commit=False)
            y.user = request.user
            y.save()
        return redirect("home")
    context = {'tasks':task ,'form':taskform}
    return render(request,"html/home.html",context)
    
def register_page(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect("login")
    else:
        user = UserCreationForm()
    return render(request, "html/register_page.html",{'form':user})

def login_page(request):
    if request.method == "POST":
        userName = request.POST['username']
        userPassword = request.POST['userpassword']
        
        if not User.objects.filter(username = userName).exists():
            return render(request,"html/login_page.html", {'error':'username not exist'})

        user = authenticate(User, username = userName ,password = userPassword)
        
        if user is None:
            return render(request,"html/login_page.html", {'error':'Pssword incorrect'})
        
        login(request,user)
        return redirect("home")
    return render(request, "html/login_page.html")
            
def logout_page(request):
    logout(request)
    return redirect("home")

@login_required
def update_task(request,pk):
    task = Task.objects.filter(user = request.user).get(id = pk)
    taskform = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST ,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request ,"html/update_task.html",{'form':taskform})
            
@login_required
def delete_task(request,pk):
    task = Task.objects.filter(user = request.user).get(id = pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,"html/delete_task.html",{'task':task})
