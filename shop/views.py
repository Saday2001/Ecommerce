from curses.ascii import HT
from operator import is_
import re
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from user.models import MyUser
from .models import Brend, Category, Clothes, Favori, Gender, Size, Commentler, Subb_category, Basket, AddImage
from django.db.models import F
from .forms import ClothesForm, CommentForm
from user.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .filters import ClothesFilter

def search_view(request):
    myclick = Clothes.objects.all().order_by('-click')
    context={"myclick":myclick}

    if request.method=='POST':
        searched = request.POST['q']
        geyimler=Clothes.objects.filter(title__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'geyimler':geyimler})
    
    else:
        return render(request, 'search.html', {}, context)

def index(request):
    context={}
    context['mydata'] = Clothes.objects.all().order_by('-created_date').exclude(author_id=request.user.id)
    context['myclick'] = Clothes.objects.all().order_by('-click').exclude(author_id=request.user.id)
    context['mydatas']=d = Clothes.objects.filter(author_id=request.user.id)
    if request.user.is_authenticated:

        context['favori_count']=Favori.objects.filter(user=request.user).count()
        context['myfavori']=Favori.objects.filter(user=request.user)
        if request.method == 'POST':
           form = ContactForm(request.POST)
           if form.is_valid():
                teklif = form.save(commit=False)
                teklif.user = request.user
                teklif.created_date = timezone.now()
                teklif.save()
                return HttpResponseRedirect('/')
        else:
            form = ContactForm()
        
        context['form'] = form
        return render(request, 'index.html', context)
      
    return render(request, 'index.html', context)

def order_click(request):
    click = Clothes.objects.all().order_by('-click').exclude(author_id=request.user.id)
    
    return render(request, 'order.html', context={'click':click})

def order_tarix(request):
    click = Clothes.objects.all().order_by('-created_date').exclude(author_id=request.user.id)

    return render(request, 'order.html', context={'click':click})

def detail(request, id):
    context={}
    geyim= get_object_or_404(Clothes, id=id)
    populars= Clothes.objects.all().order_by('-created_date').exclude(pk = geyim.id)
    geyim.click=F('click')+1
    geyim.save(update_fields=['click'])
    comments = geyim.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = geyim
            new_comment.user = request.user
            new_comment.save()
            return  redirect('blog:detail',id=id)
    else:
        form = CommentForm()
        context['form'] = form

    comments = Commentler.objects.filter(post=geyim)
    context['comments'] = comments.order_by('-id')
    context['geyim']=geyim
    context['populars']=populars
    return render(request,'detail.html',context)

def shop(request):
    geyimler = Clothes.objects.all().exclude(author_id=request.user.id)
    geyim_filter = ClothesFilter(request.GET, queryset=geyimler)

    filter_data = {}
    for key, val in dict(geyim_filter.data).items():
        if type(val) == list:
            filter_data[key] = ",".join(i for i in val)
        else:
            filter_data[key] = val
    


    p=Paginator(geyim_filter.qs, 2)
    page = request.GET.get('page')
    clothes = p.get_page(page)
    

    context = {
        "clothes":clothes,
        "geyim_filter":geyim_filter,
        "filter_data": filter_data.items()
    }

    return render(request, 'shop.html', context)


def category_view(request, id):
    category_s = get_object_or_404(Category,id=id)
    venues = category_s.category_geyim.filter(draft=True).exclude(author_id=request.user.id)

    p=Paginator(category_s.category_geyim.filter(draft=True), 8)
    page = request.GET.get('page')
    venues = p.get_page(page)

    context = {
        'category':category_s,
        "venues":venues
    }

    return render(request, 'categoies.html', context)

def subb_category(request, id):
    subb_s = get_object_or_404(Subb_category,id=id)
    venues = subb_s.subb_geyim.filter(draft=True).exclude(author_id=request.user.id)

    print(subb_s)

    p=Paginator(subb_s.subb_geyim.filter(draft=True), 8)
    page = request.GET.get('page')
    venues = p.get_page(page)
    
    context = {
        'subb':subb_s,
        "venues":venues
        
    }

    return render(request, 'categoies.html', context)


def marka_view(request, id):
    marka_s=get_object_or_404(Brend, id=id)
    venues = marka_s.brend_geyim.filter(draft=True).exclude(author_id=request.user.id)

    p=Paginator(marka_s.brend_geyim.filter(draft=True), 8)
    page = request.GET.get('page')
    venues = p.get_page(page)

    context={
        "marka_s":marka_s,
        "venues":venues
    }

    return render(request, 'categoies.html', context)


def gender_view(request, id):
    gender_s=get_object_or_404(Gender, id=id)
    venues = gender_s.gender_clothes.filter(draft=True).exclude(author_id=request.user.id)

    p=Paginator(gender_s.gender_clothes.filter(draft=True), 4)
    page = request.GET.get('page')
    venues = p.get_page(page)

    context={
        "venues":venues,
        "gender_s":gender_s,
    }

    return render(request, 'categoies.html', context)


def Addclothes(request):
    context = {}

    if request.method == 'POST':
        form = ClothesForm(request.POST or None)
        images = request.Files.getlist('images', None)
        if form.is_valid() and images:
            geyim = form.save(commit=False)
            geyim.author = request.user
            geyim.created_date = timezone.now()
            geyim.save()

            for image in images:
                geyim_image = AddImage.objects.all(
                    product = geyim, image=image
                )
            messages.success(request, ' Geyiminizi uğurla əlavə etdiniz!')
            return HttpResponseRedirect('/')

    else:
        form = ClothesForm()
        
    context['form'] = form
    return render(request, 'add.html', context)


def dashboard(request, id):
    user_s = get_object_or_404(MyUser, id=id)
    geyim = user_s.user_geyim.filter(draft=True).order_by('-created_date')

    context={
        "geyim":geyim
    }

    return render(request, 'dashboard.html', context)

def test(request, id):
    geyimler = Clothes.objects.filter(author_id = id).exclude(author_id=request.user.id)

    return render(request, 'test.html', context={'geyimler':geyimler})

def addfavori(request, id):
    obj = get_object_or_404(Clothes, id=id)
    if not Favori.objects.filter(geyim=obj,user=request.user).exists():
        Favori.objects.create(geyim=obj,user=request.user)
    else:
        Favori.objects.filter(geyim=obj,user=request.user).delete()

    return redirect('blog:favorilist')

def deletefavori(request, id):
    obj = get_object_or_404(Clothes, id=id)
    
    Favori.objects.filter(geyim=obj, user=request.user).delete()

    return redirect('blog:favorilist')

def Favorilist(request):
    if request.user.is_authenticated:
       user = request.user

       listl = Favori.objects.filter(user=user)

       context={
           "listl":listl
       }

       return render(request, 'wishlist.html', context)
    return render(request, 'wishlist.html')

def addbasket(request, id):
    obj = get_object_or_404(Clothes, id=id)
    if not Basket.objects.filter(geyim=obj,user=request.user).exists():
        Basket.objects.create(geyim=obj,user=request.user)

    return redirect('blog:basket')

def deletebasket(request, id):
    obj = get_object_or_404(Clothes, id=id)
    
    Basket.objects.filter(geyim=obj, user=request.user).delete()

    return redirect('blog:basket')

def Basketlist(request):
    if request.user.is_authenticated:
        user = request.user

        basket_list = Basket.objects.filter(user=user)


        context={
            "basket_list":basket_list,
        }

        return render(request, 'cart.html', context)
    
    return render(request, 'cart.html')


def delete_baza(request, id):
    
    geyim = get_object_or_404(Clothes, id=id, author_id = request.user.id)

    Clothes.objects.filter(id=geyim.id).delete()

    return redirect('blog:index')