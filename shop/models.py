from re import M
from turtle import onclick
from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.Model):
    title = models.CharField(_('Ad'), max_length=25)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Brend(models.Model):
    title = models.CharField(_('Ad'), max_length=25)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_('Ad'), max_length=25)
    def __str__(self):
        return self.title

class Subb_category(models.Model):
    title = models.CharField(_('Ad'), max_length=25)
    category=models.ForeignKey('Category', on_delete=models.CASCADE,related_name='category')

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(_('Ad'), max_length=25)

    def __str__(self):
        return self.title

class Clothes(models.Model):
    author=models.ForeignKey('user.MyUser', on_delete=models.CASCADE, related_name='user_geyim')
    title = models.CharField(max_length=25)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE,related_name='gender_clothes')
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE, null=True, blank=True, related_name='brend_geyim')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name="category_geyim")
    subb = models.ForeignKey('Subb_category', on_delete=models.CASCADE, related_name='subb_geyim')
    size=models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
    color = models.ForeignKey('Color',on_delete=models.CASCADE )
    about = models.TextField(null=True)
    cost = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    click=models.IntegerField(default=0, editable=False)
    draft = models.BooleanField(default=True,null=True)
    

    def __str__(self):
        return self.title

    def main_product_image(self):
        product_images = AddImage.objects.filter(product = self)

        if product_images.exists():
            return product_images.first().image.url
        
        return '-'
    

class AddImage(models.Model):
    product = models.ForeignKey('Clothes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title or self.id



class Commentler(models.Model):
    user = models.ForeignKey('user.MyUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Clothes,null=True,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Commentler {} by {}'.format(self.body, self.user.username)

class Favori(models.Model):
    user = models.ForeignKey('user.MyUser',on_delete=models.CASCADE)
    geyim = models.ForeignKey('Clothes', on_delete=models.CASCADE,related_name="clothes_add")

    def __str__(self):
        return str(self.geyim)

class Basket(models.Model):
    user = models.ForeignKey('user.MyUser',on_delete=models.CASCADE)
    geyim = models.ForeignKey('Clothes', on_delete=models.CASCADE, related_name='geyim_basket')
    draft = models.BooleanField(default=True,null=True)
    
    def __str__(self):
        return str(self.geyim)


