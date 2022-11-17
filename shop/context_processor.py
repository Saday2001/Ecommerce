from .models import Gender, Category, Brend, Subb_category, Size, Favori, Basket, Commentler

def extras(request):
    context={}
    context['genders'] = Gender.objects.all()
    context['categories'] = Category.objects.all()
    context['markas']=Brend.objects.all()
    context['subb'] = Subb_category.objects.all()
    context['sizes'] = Size.objects.all()
    if request.user.is_authenticated:

        context['favori_count']=Favori.objects.filter(user=request.user).count()
        context['myfavori']=Favori.objects.filter(user=request.user)
        context['basket_count']=Basket.objects.filter(user=request.user).count()
    
    return context