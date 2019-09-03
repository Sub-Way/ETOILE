from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from photo.models import Album, Photo, Categories, Cart, Buy , order_value, CartItem,order_list
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from HOME.views import LoginRequiredMixin

from django.shortcuts import redirect
from photo.forms import PhotoInlineFormSet
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required
class MbagLV(ListView):
    template_name = "photo/m_bag.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='m_bag')


class MclothLV(ListView):
    template_name = "photo/m_cloth.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='m_cloth')

class MfashionLV(ListView):
    template_name = "photo/m_fashion.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='m_fashion')

class MshoeLV(ListView):
    template_name = "photo/m_shoe.html"
    model = Album
    def get_queryset(self):
        return Album.objects.filter(Category__title='m_shoe')

class MwalletLV(ListView):
    template_name = "photo/m_wallet.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='m_wallet')


class WbagLV(ListView):
    template_name = "photo/w_bag.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='w_bag')


class WclothLV(ListView):
    template_name = "photo/w_cloth.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='w_cloth')


class WfashionLV(ListView):
    template_name = "photo/w_fashion.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='w_fashion')


class WshoeLV(ListView):
    template_name = "photo/w_shoe.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='w_shoe')
class WwalletLV(ListView):
    template_name = "photo/w_wallet.html"
    model = Album

    def get_queryset(self):
        return Album.objects.filter(Category__title='w_wallet')


class AlbumLV(ListView):
    model = Album


class Category(DetailView):
    model = Categories


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo

    def albums(self):
        return Album.objects.all()#filter(Album__name=self.object.album)

    def get_context_data(self, **kwargs):
        context = super(testView, self).get_context_data(**kwargs)
        context['extra_value'] = Album.objects.all()
        return context

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instace.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')


class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['name', 'description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self,form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class testView(ListView):
    model = Photo
    template_name = 'photo/photo_detail.html'
    context_object_name = 'main_list'


    def get_context_data(self, **kwargs):
        context = super(testView, self).get_context_data(**kwargs)
        context['extra_value'] = Album.objects.all()
        return context


def album_detail(request, album_id):
    albumObj = get_object_or_404(Album, pk=album_id)
    return render(request, 'photo/album_detail.html', {'albumObj': albumObj})

@login_required
def CartOrBuy(request):
    size = request.POST.get('Size')
    Num = request.POST.get('CNum')
    UID = request.POST.get('URLID')
    if request.POST:
        if 'Buy' in request.POST:
            product=Album.objects.get(id=UID)
            new_order = Buy.objects.create(product =product)
            new_order.quantity= Num
            new_order.Csize = size
            new_order.save()
            return render(request, 'HOME/order.html', {'ob': new_order})

        elif 'Cart' in request.POST:
            request.session.set_expiry(12000)
            try:
                the_id = request.session['cart_id']
            except:
                new_cart = Cart()
                new_cart.save()
                request.session['cart_id'] =new_cart.id
                the_id = new_cart.id
            cart = Cart.objects.get(id=the_id)

            product= Album.objects.get(id=UID)

            cart_item = CartItem.objects.create(cart=cart,product=product)
            cart_item.quantity = Num
            cart_item.Csize = size
            cart_item.save()
            # bids = Cart(album=UID,owner=request.user, update_date=datetime.now(), quantity=Num,Csize=size)
            # bids.save()
            return HttpResponseRedirect(reverse("photo:cartbag"))
            # return render(request, 'HOME/cart.html', {'ob': Cart,'Album':Album})
    elif request.GET:
        return render(request, 'HOME/cart.html')
    return render(request, 'HOME/cart.html')

@login_required
def view(request):
    # 세션 추가(회원별 장바구니를 위해)
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        # 장바구니 가격 계산, 여기서 item은 class CartItem의 instance가 된다
        new_total = 0
        for item in cart.cartitem_set.all():  # foreignkey를 통해 class cartitem을 전부 끄집어내는 접근법
            line_total = int(item.product.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()  # 장바구니 갯수 새기
        cart.total = new_total
        cart.save()  # 장바구니 데이터베이스에 저장
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}

    template = 'HOME/cart.html'
    return render(request, template, context)


def remove_from_cart(request, id):


	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("photo:cartbag"))

	cartitem = CartItem.objects.get(id=id)
	 #cartitem.delete()
	cartitem.cart = None
	cartitem.save()
	#send "success message"
	return HttpResponseRedirect(reverse("photo:cartbag"))

def orderlist(request):
    template = 'HOME/order.html'
    return render(request, template)


def sendorderlist(request):
    size = request.POST.get('Csize')
    Num = request.POST.get('quantity')
    name1 = request.POST.get('name1')
    mail1 = request.POST.get('mail1')
    phone1 = request.POST.get('phone1')
    phone2 = request.POST.get('phone2')
    phone3 = request.POST.get('phone3')

    name2 = request.POST.get('name2')
    phone4 = request.POST.get('phone4')
    phone5 = request.POST.get('phone5')
    phone6 = request.POST.get('phone6')

    add1 = request.POST.get('add1')
    add2 = request.POST.get('add2')
    add3 = request.POST.get('add3')
    memo = request.POST.get('memo')
    AID = request.POST.get('URLID')
    product = Album.objects.get(id=AID)
    cart_item = order_list.objects.create(
    owner=request.user,
    name1=name1,
    mail1 = mail1,
    phone1 = phone1,
    phone2 = phone2,
    phone3 = phone3,

    name2 = name2,
    phone4 = phone4,
    phone5 = phone5,
    phone6 = phone6,

    add1 = add1,
    add2 = add2,
    add3 = add3,
    memo = memo,
    product=product
    )
    template = 'HOME/index.html'
    return render(request, template)


def cartorderlist(request):
    try:
        the_id = request.session['cart_id']
        order = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("photo:cartbag"))

    return render(request, 'HOME/order2.html', {'ob': order})

def sendorderlist2(request):
    template = 'HOME/index.html'

    name1 = request.POST.get('name1')
    mail1 = request.POST.get('mail1')
    phone1 = request.POST.get('phone1')
    phone2 = request.POST.get('phone2')
    phone3 = request.POST.get('phone3')

    name2 = request.POST.get('name2')
    phone4 = request.POST.get('phone4')
    phone5 = request.POST.get('phone5')
    phone6 = request.POST.get('phone6')

    add1 = request.POST.get('add1')
    add2 = request.POST.get('add2')
    add3 = request.POST.get('add3')
    memo = request.POST.get('memo')
    cartid = request.POST.get('cartid')
    CartInfo = Cart.objects.get(id=cartid)
    for Cart3 in CartInfo.cartitem_set.all():
        print("gg")
        order_list.objects.create(
            owner=request.user,
            name1=name1,
            mail1=mail1,
            phone1=phone1,
            phone2=phone2,
            phone3=phone3,
            name2=name2,
            phone4=phone4,
            phone5=phone5,
            phone6=phone6,
            add1=add1,
            add2=add2,
            add3=add3,
            memo=memo,
            product=Cart3.product

        )

        return render(request, template)
