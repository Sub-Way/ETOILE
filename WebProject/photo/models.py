from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from photo.fields import ThumbnailImageField
from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible
class SecondAlbumManager(models.Manager):
    def get_queryset(self):
        return super(SecondAlbumManager, self).get_queryset().filter(Categories_title='m_bag')

class Categories(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('photo:Categories_detail', args=(self.id,))
@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE,)
    price = models.CharField(max_length=20, null=True)
    productInfo = models.CharField(max_length=300, null=True)
    WorM = models.BooleanField(default=True)
    objects = models.Manager()
    second_manager = SecondAlbumManager()

    class Meta:
        ordering = ['Category']
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    class Meta:
        ordering = ['title']
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:test', args=(self.id,))


class Cart(models.Model):
    total = models.IntegerField(default=0)
    update_date= models.DateTimeField(auto_now_add=False,auto_now=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)

    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    class Meta:
        ordering = ['update_date']
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,null=True,blank=True, on_delete=models.CASCADE,)
    product = models.ForeignKey(Album, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    Csize = models.CharField(max_length=5, default='M')
    line_total = models.IntegerField(default=0)
    update_date = models.DateTimeField('Update Date', auto_now=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)
    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title

class Buy(models.Model):
    product = models.ForeignKey(Album, on_delete=models.CASCADE,)
    # cart = models.ForeignKey(Cart)
    # price = models.IntegerField(default=0)
    order_date = models.DateTimeField('order_date', auto_now=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    Csize = models.CharField(max_length=5,default='M')
    class Meta:
        ordering = ['order_date']

class order_value(models.Model):
    price = models.IntegerField(default=0)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)

class order_list(models.Model):
    order_date = models.DateTimeField('order_date', auto_now=True)
    product = models.ForeignKey(Album, on_delete=models.CASCADE,)
    name1= models.CharField(max_length=100)
    mail1=models.CharField(max_length=100)
    phone1= models.CharField(default='010',max_length=3)
    phone2 = models.CharField(default='2050',max_length=4)
    phone3 = models.CharField(default='8194',max_length=4)

    name2 = models.CharField(max_length=100)

    phone4 = models.CharField(default='010',max_length=3)
    phone5 = models.CharField(default='3524',max_length=4)
    phone6 = models.CharField(default='6342',max_length=4)

    add1= models.CharField(max_length=100)
    add2= models.CharField(max_length=100)
    add3= models.CharField(max_length=100)

    memo= models.TextField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)
    class Meta:
        ordering = ['order_date']
        verbose_name = 'order'
        verbose_name_plural = 'orders'
