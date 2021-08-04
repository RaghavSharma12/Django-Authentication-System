from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request,"index.html")
    
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        # check user has entered correct credentials
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
    # No backend authenticated the credentials
              return render(request ,"login.html")
    return render(request ,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")

