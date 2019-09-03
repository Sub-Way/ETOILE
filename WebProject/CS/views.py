from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import TodayArchiveView

from CS.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from HOME.views import LoginRequiredMixin
from django.views.generic.edit import FormView
from CS.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
from photo.models import Album, Photo, Categories

class PostLV(ListView):
    model = Post
    template_name = 'CS/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'
    # 대상 table


class PostDV(DetailView):
    model = Post


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    initial = {'slug': 'auto-filling-do-not-input'}
    # fields = ['title', 'description', 'content', 'tag]
    success_url = reverse_lazy('CS:post_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'CS/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    success_url = reverse_lazy('CS:post_list')


class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('CS:post_list')




# ------------------------------------------------------------------------------------


def SearchFormView(request):
    product = request.POST['search']
    products = Album.objects.filter(Q(name__icontains=product)).distinct()
    return render(request, 'CS/post_search.html', {'product': products})

def SearchPostView(request):
    entry_title = request.POST['searchPost']
    post = Post.objects.filter(Q(title__icontains=entry_title)).distinct()
    return render(request, 'CS/post_search2.html', {'ob': post})
