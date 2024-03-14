from django.shortcuts import render
from users.forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'Index.html')
def aboutus(request):
    return render(request, 'Aboutus.html')
def contact(request):
    return render(request, 'Contact.html')
def register(request):
    return render(request, 'Register.html')
def login(request):
    form = StudentForm()
    return render(request, 'Login.html',context = {'form':form})