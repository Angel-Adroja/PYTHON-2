from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'GET':
        form=UserCreationForm()
        return render(request, 'signup.html',{'form':form})
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'signup.html',{'form':form})
def loginacc(request):
    form=AuthenticationForm()
    if request.method=="GET":
        return render (request,'login.html',{'form':form})
    elif request.method=="POST":
        user=authenticate(request,
                          username=request.POST['username'],
                          password=request.POST['password'])   
        if user is None:
            error="The username or password is incorrect"
            return render (request,'login.html',{'form':form,'error':error})
        else:
            login(request,user)
            return redirect('home')
        
def logoutacc(request):
    logout(request)
    return redirect('home')       
          
@login_required

def student(request):
    s=Student.object.all()
    return render(request,'student.html',{'s':s})