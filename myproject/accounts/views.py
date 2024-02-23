# from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.shortcuts import render,redirect

# def login_user(request):
#     if request.method == "POST":
#         usernames = request.POST["username"]
#         passwords = request.POST["password"]
        
#         user = authenticate(request, username = usernames, password = passwords)
        
#         if user is not None:
#             login(request, user)
#             return redirect("myapp:index")
#         else:
#             messages.info(request, "Identifiant ou mot de passe incorrect")
        
#     form = AuthenticationForm()
#     return render(request,"page/login.html",{'form':form})

# def logout_user(request):
#     logout(request)
#     return redirect("myapp:index")

# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:index')
#     form = UserCreationForm() 
#     return render(request,"page/register.html",{"form": form})

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("myapp:index")
        else:
            messages.info(request,'mot de passe ou Identifiant incorrect')
    
    form = AuthenticationForm()
    return render(request,"page/login.html",{"form": form})

def logout_user(request):
    logout(request)
    return redirect("myapp:index")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = UserCreationForm()
    return render(request,"page/register.html",{"form": form})