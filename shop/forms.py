from django import forms
from .models import Clothes, Commentler

class ClothesForm(forms.ModelForm):

    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control   ',
        'placeholder':'Ad',
        
        }
    ))
    
    about = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control ',
        'placeholder':'Haqqında',
        }
    ))

    cost = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control ',
        'placeholder':'Qiymət',
        }
    ))
    
    class Meta:
        model=Clothes

        fields=['title', 'gender', 'brend', 'category', 'subb', 'size', 'color', 'about', 'cost']
    

    def __init__(self, *args, **kwargs):
        super(ClothesForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
            "class": "form-control",

        })

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'cols':'150',
        'rows':'0',
        'placeholder':'Rey yazin...',
        }
    ))
    
    class Meta:
        model = Commentler
        fields= ['body']


