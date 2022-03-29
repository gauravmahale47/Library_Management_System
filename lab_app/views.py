from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def registration(req):
    if req.method=='POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Congratulations, your account has been successfully created. Please Login.')
            return redirect('login')
    elif req.method=='GET':
        form = CustomUserCreationForm()
    data = {'form':form}
    return render(req,'registration.html', data )


from .forms import MyAuthenticationForm
from django.contrib.auth import authenticate,login,logout
def mylogin(req):
    if req.method=='GET':
        form = MyAuthenticationForm()
    elif req.method=='POST':
        form = MyAuthenticationForm(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(email=username,password=password)
        if user is not None:
            login(req,user)
            return redirect(index)
        else:
            messages.error(req,'Invalid Username or Password') 
    data = {'form':form}
    return render(req,'login.html',data)

@login_required(login_url='/login')
def mylogout(req):
    logout(req)
    messages.success(req,'Logout Successfully....')
    return redirect('login')


def index(request):
    return render(request, 'index.html')


from .models import Books
@login_required(login_url='/login')
def book_list(request):
    books = Books.objects.all()
    return render(request,'list.html', {'books':books})

@login_required(login_url='/login')
@permission_required('lab_app.add_books')
def add(request):
    if request.method == "POST":
        bname = request.POST['bname']
        bcategory = request.POST['bcategory']
        bauthor = request.POST['bauthor']
        bprice = request.POST['bprice']
        Books.objects.create(Book_Name=bname, Book_Category=bcategory, Book_Author=bauthor, Book_Price=bprice)
        return redirect(book_list)

@login_required(login_url='/login')
@permission_required('lab_app.delete_books')
def delete(request, id):
    book = Books.objects.get(Id=id)
    book.delete()
    return redirect(book_list)

@login_required(login_url='/login')
@permission_required('lab_app.change_books')
def edit(request,id):
    books = Books.objects.all()
    data = Books.objects.get(Id=id)
    return render(request,'edit.html',{'data':data, 'books':books})

@login_required(login_url='/login')
@permission_required('lab_app.change_books')
def update(request):
    if request.method == "POST":
        id = request.POST['bid']
        bname = request.POST['bname']
        bcategory = request.POST['bcategory']
        bauthor = request.POST['bauthor']
        bprice = request.POST['bprice']
        book = Books.objects.filter(Id=id)
        book.update(Id=id,Book_Name=bname, Book_Category=bcategory, Book_Author=bauthor, Book_Price=bprice)
        return redirect(book_list)