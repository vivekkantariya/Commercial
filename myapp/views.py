from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from .models import BookFree
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection as conn

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'Aboutus.html')

def Salary_based_attendance(request):
    return render(request,'salarybasedattendance.html')

def AssignTask(request):
    return render(request,'assigntask.html')

def LeaveManage(request):
    return render(request,'leavemanage.html')

def AttendanceManage(request):
    return render(request,'attendancemanage.html')

def Contact(request):
    return render(request,'contact.html')

def Freedemo(request):
    return render(request,'freedemo.html')

def CongratsFree(request):
    return render(request,'congratsfree.html')

def bookfree(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            # code to save the data in the database using sql
            query = "INSERT INTO admin_login (username, password) VALUES ('{}', '{}')".format(email, password)
            with conn.cursor() as cursor:
                row_affected = cursor.execute(query)
                conn.commit()
            
            if row_affected > 0:
                return redirect('congratsfree')
            else:
                return redirect('bookfree.html', {'error': 'Some error occurred. Please try again.'})
        else:
            return render(request, 'bookfree.html', {'error': 'Start'})
    except Exception as e:
        print(e)
        return render(request, 'bookfree.html', {'error': 'You are already registered. Please login.'})
def trynow(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']

        book_free = BookFree.objects.create(full_name=full_name, email=email)

        return redirect(request, 'congratsfree.html', {'book_free': book_free})
    else:
        return render(request, 'bookfree.html')

def Payment(request):
    if request.method == 'POST':
        payment_success = True  # or False based on your logic
        return render(request, 'success_page.html', {'payment_success': payment_success})
    else:
        return render(request, 'payment.html')

def success_page(request):
    return render(request, 'success_page.html', {'payment_success': True})

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_page.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page upon successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
