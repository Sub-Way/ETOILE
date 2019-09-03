from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from HOME.views import *
from CS.models import Post
from photo.models import Album, Photo, Categories, Cart, Buy , order_value, CartItem,order_list
from django.db.models import Q
from django.views.generic import *
import operator
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from HOME.forms import SignupForm, UpdateProfile, UserForm
from django.contrib.auth.models import User
from HOME.models import temp
from django.views.generic.edit import UpdateView
from django.template import loader, Context ,RequestContext
from django.urls import resolve
# Create your views here.


# class HomeView(TemplateView):
# template_name = 'HOME/index.html'

def index(request):
    return render(request, 'HOME/index.html')


def man(request):
    return render(request, 'HOME/man.html')


def woman(request):
    return render(request, 'HOME/woman.html')

# def MypageView(request):
    #form = MypageForm(initial={'email': request.user.email,'username':request.user.username})
    #return render(request, "HOME/mypage.html", {
   #     "form": form,
     #   })

def signup(request):

    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect(
                reverse("HOME:signup_ok")

            )
    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "registration/register.html", {
        "signupform": signupform,
        })

    """template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:register_done')"""

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignupForm
    success_url = reverse_lazy("HOME:signup_ok")
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logged_out.html')

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class legal(TemplateView):
    template_name = 'registration/legal.html'

@login_required
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user, initial={'username':request.user.username})
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'HOME/mypage.html', args)

def orderlist(request):
    OL= order_list.objects.filter(owner=request.user)
    return render(request, 'HOME/orderlist.html', {'OB': OL})
