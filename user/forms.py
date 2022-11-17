from curses.ascii import CR
from django import forms
from .models import MyUser, Contact
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'class':'form-control   ',
        
        }
    ))
    class Meta:
        model = User
        fields= ('email','username','phone', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')


    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')


class LoginForm(forms.Form):

    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    class Meta:
        model = MyUser
        fields= ['email','password']

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    surname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control   ',
        
        }
    ))


    
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control   ',
        
        }
    ))

    class Meta:
        model = Contact
        fields= ['name', 'surname', 'body']
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
            "class": "form-control",

        })
