from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def login(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_data = Admin.objects.filter(username=username, password=password)
        if user_data:
            request.session['name'] = 'username'
            return redirect( '/')
        else:
            print("invalid")
            return render(request, 'login_admin.html', {'status': "invalid"})
    return render(request, 'login_admin.html')


def logout(request):
    del request.session['name']
    return redirect('/login')

def signin(request):
    if request.method == "POST":
        names = request.POST.get("name")
        emails = request.POST.get("email")
        usernames = request.POST.get("username")
        passwords = request.POST.get("password")
        print(names, emails, usernames, passwords)
        data = Admin()
        data.name = names
        data.email = emails
        data.username = usernames
        data.password = passwords
        data.save()
        return redirect("/")

    return render(request, 'signin.html')

def welcome(request):
    user_data = Admin.objects.all()
    return render(request, 'hello.html', {'user':user_data})

