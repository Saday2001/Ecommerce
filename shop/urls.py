from django.urls import path
from .views import *
app_name= 'blog'

urlpatterns = [
   path('', index, name='index'),
   path('geyim<int:id>/', detail, name='detail'),
   path('shop/', shop, name='shop'),
   path('category<int:id>/', category_view, name='product_categories'),
   path('subb<int:id>/', subb_category, name='subb_view'),
   path('marka<int:id>/', marka_view, name='marka_view'),
   path('gender<int:id>/', gender_view, name='gender_view'),
   path('add/', Addclothes, name='add'),
   path('search/', search_view, name='search_view'),
   path('dashboard<int:id>/', dashboard, name='dashboard'),
   path('click/', order_click, name='orderclick'),
   path('date/', order_tarix, name='orderdate'),
   path('test<int:id>/', test, name='test'),
   path('fav<int:id>/', addfavori, name='addfavori'),
   path('favori/', Favorilist, name='favorilist'),
   path('delete<int:id>/', deletefavori, name='deletefav'),
   path('basket<int:id>/', addbasket, name='addbasket'),
   path('basket/', Basketlist, name='basket'),
   path('deletebasket<int:id>/', deletebasket, name='deletebasket'),
   path('deletebaza<int:id>/', delete_baza, name='delete_baza')

]