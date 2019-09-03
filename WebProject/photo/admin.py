from django.contrib import admin
from photo.models import Album, Photo, Categories, Cart, Buy , order_value, CartItem,order_list
# Register your models here.
from photo.models import Cart

class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2


class CategoriesAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    list_display = ('title',)


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


class CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart
class BuyAdmin(admin.ModelAdmin):
    class Meta:
        model = Buy

class order_valueAdmin(admin.ModelAdmin):
    class Meta:
        model =order_value
class order_listAdmin(admin.ModelAdmin):
    class Meta:
        model= order_list

admin.site.register(order_list,order_listAdmin)
admin.site.register(order_value, order_valueAdmin)
admin.site.register(Buy, BuyAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)

