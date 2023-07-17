from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import SignUpForm, AddRecordForm




# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method=='POST':
       username=request.POST['Username']
       password=request.POST['Password']

       user=authenticate(request,username=username ,password=password )
       if user is not None:
           login(request,user)
           messages.success(request,"Iniciaste Sesion!")
           return redirect('home')
       else:
           messages.success(request,"Nombrede Usuario O Contraseña son incorrectos, Por favor Intente Nuevamente...")
           return redirect('home')
    else:
        return render(request, 'home.html',{'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"Cerrando Sesion")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "¡Se ha registrado exitosamente! Bienvenido")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Debe iniciar sesión para ver esa página...")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')