from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}))
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))

class Meta():
    model= User
    fields=('username','first_name','last_name','email','password1','password2')

def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
		self.fields['username'].label = ''
		self.fields['username']

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1']
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que antes, para verificación.</small></span>'


class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)	