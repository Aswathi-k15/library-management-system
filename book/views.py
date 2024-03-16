
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

def register(request):
    if request.method == "POST":
        names = request.POST.get("name")
        usernames = request.POST.get("username")
        passwords = request.POST.get("password")
        emails = request.POST.get("email")
        phonenumbers = request.POST.get("phone_number")
        data = Author()
        data.name = names
        data.username = usernames
        data.password = passwords
        data.email = emails
        data.phone_number = phonenumbers
        data.save()
        return redirect("/view_author")

    return render(request, 'register_author.html')

def a_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_data = Author.objects.filter(username=username, password=password)
        if user_data:
            return render(request, 'home1.html', {'user': user_data})
        else:
            print("invalid")
            return render(request, 'login_author.html', {'status': "invalid"})
    return render(request, 'login_author.html')

def register_user(request):
    if request.method == "POST":
        names = request.POST.get("name")
        usernames = request.POST.get("username")
        passwords = request.POST.get("password")
        emails = request.POST.get("email")
        phonenumbers = request.POST.get("phone_number")
        data = User()
        data.name = names
        data.username = usernames
        data.password = passwords
        data.email = emails
        data.phone_number = phonenumbers
        data.save()
        return redirect("/view_user")

    return render(request, 'register_user.html')

def u_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_data = User.objects.filter(username=username, password=password)
        if user_data:
            return render(request, 'home2.html', {'user': user_data})
        else:
            print("invalid")
            return render(request, 'login_user.html', {'status': "invalid"})
    return render(request, 'login_user.html')

def a_show(request):
    user_data = Author.objects.all()
    return render(request, 'view_author.html', {'user': user_data})

def a_edit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        data = Author.objects.get(id=id)
        data.name = request.POST.get('name')
        data.username = request.POST.get('username')
        data.password = request.POST.get('password')
        data.email = request.POST.get('email')
        data.phone_number = request.POST.get('phone_number')
        data.save()
        return redirect('/view_author')
    user_data = Author.objects.filter(id=id)
    return render(request, 'edit_author.html', {'author': user_data})

def a_remove(request, id):
    user_data = User.objects.get(id=id)
    user_data.delete()
    return redirect('/view_user')
def home1(request):
    abcd=Author.objects.all()
    return render(request,'home1.html',{'abcde':abcd})

def home2(request):
    h2=User.objects.all()
    return render(request,'home2.html',{'hm2':h2})
def viewuser(request):
    user_data = User.objects.all()
    return render(request, 'view_user.html', {'user': user_data})

def u_edit(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        data = User.objects.get(id=id)
        data.name = request.POST.get("name")
        data.username = request.POST.get("username")
        data.password = request.POST.get("password")
        data.email = request.POST.get("email")
        data.phone_number = request.POST.get("phone_number")
        data.save()
        return redirect('/view_user')
    user_data = User.objects.filter(id=id)
    return render(request, 'edit_user.html', {'user':user_data})

def u_remove(request, id):
    user_data = User.objects.get(id=id)
    user_data.delete()
    return redirect('/view_user')
def add_book(request):
    print("KK")
    print(request.method)
    if request.method == "POST":
        booknames=request.POST.get("bookname")
        authors = request.POST.get("author")
        categorys = request.POST.get("category")
        descriptions = request.POST.get("description")
        pub_dateww = request.POST.get("published_date")
        prices = request.POST.get("price")
        images = request.POST.get("upload_image")
        print(categorys,booknames, authors, pub_dateww,descriptions,prices,images)
        data = Book()
        data.bookname=booknames
        data.author = authors
        data.category = categorys
        data.description = descriptions
        data.published_date = pub_dateww
        data.price = prices
        data.upload_image = images
        data.save()
        return redirect("/")
    return render(request, 'add_book.html')
def viewbook(request):
    print("home fun called")
    book_data = Book.objects.all()
    return render(request, 'view_book.html', {'book': book_data})
def remove(request, id):
    print("remove fun called")
    book_data = Book.objects.get(id=id)
    book_data.delete()
    return redirect('/view_book')


def edit(request, id):
    print("edit fun called")
    if request.method == "POST":
        print("now method is post")
        bookname = request.POST.get('bookname')
        print("bookname : " ,bookname)
        data = Book.objects.get(id=id)
        data.bookname = request.POST.get("bookname")
        data.author = request.POST.get("author")
        data.category = request.POST.get("category")
        data.description = request.POST.get("description")
        data.published_date = request.POST.get("published_date")
        data.price = request.POST.get("price")
        data.upload_image = request.POST.get("upload_image")
        data.save()
        return redirect('/view_book')
    user_data = Book.objects.filter(id=id)
    return render(request, 'edit_book.html', {'book': user_data})

def home(request):
    if 'name' in request.session:
        user = request.session['name']
        book_data = Book.objects.all()
        categorys=Book.objects.all()
        prices=Book.objects.all()
        if request.method=="POST":
            search = request.POST.get('bookname')
            if search:
                book_data=Book.objects.filter (Q(bookname__icontains=search)| Q(author__icontains=search)| Q(description__icontains=search)| Q(category__icontains=search)| Q(price__icontains=search) )
        elif 'category' in request.GET:
                categorys = request.GET['category']
                book_data = Book.objects.filter(category__icontains=categorys)
        elif 'price' in request.GET:
            prices=request.GET['price']
            print(prices)
            book_data=Book.objects.filter(price__lte=int(prices))

        return render(request, 'home.html',{'user': user, 'book': book_data, 'category': categorys, 'price':prices })
    else:
        print("ooo")
        return redirect('/login')
