from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Article, Category, Tag
from .forms import RegisterForm, LoginForm, EditUserForm, EditPasswordForm, CategoryForm, ArticleSearchForm, TagForm

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser, login_url='/')(view_func)
    return decorated_view_func

def index(request):
    login_form = LoginForm()
    register_form = RegisterForm()
    if request.method == 'POST':
        if 'login-submit' in request.POST:
            login_form = LoginForm(request.POST)

            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('products')

        elif 'register-submit' in request.POST:
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                user = register_form.save()
                user.set_password(register_form.cleaned_data.get('password'))
                user.save()

                login(request, user)
                return redirect('home')
        elif 'logout' in request.POST:
            return redirect('logout')
    return render(request, 'index.html', {'login_form': login_form, 'register_form': register_form})

def contact(request):
    return render(request, 'contact.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def products(request):
    form_article = ArticleSearchForm(request.GET or None)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if form_article.is_valid():
        articles = form_article.search_articles()
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'form_article': form_article, 'tags': tags, 'categories': categories}
    return render(request, 'products.html', context)

@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        password_form = EditPasswordForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito!')
            return redirect('home')
    else:
        user_form = EditUserForm(instance=request.user)
        password_form = EditPasswordForm(request.user)
    return render(request, 'user_edit.html', {'user_form': user_form, 'password_form': password_form})

class LogoutView(TemplateView):
    template_name = 'logout.html'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('index'))

@superuser_required
def category_new(request):
    template_name = 'categories/category_new.html'
    form = CategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    context = {
        'form': form,
        'title': 'Create Category'
    }
    return render(request, template_name, context)

@superuser_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=pk)
    else:
        form = CategoryForm(instance=category)
    context = {
        'category': category,
        'form': form
    }
    return render(request, 'categories/category_edit.html', context)

@superuser_required
def category_list(request):
    template_name = 'categories/category_list.html'
    categories = Category.objects.all().order_by('-created_at')
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

@superuser_required
def category_detail(request, pk):
    template_name = 'categories/category_detail.html'
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category
    }
    return render(request, template_name, context)

@superuser_required
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')





@superuser_required
def tag_new(request):
    form = TagForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tag_list')
    context = {
        'form': form,
        'title': 'Create Tag'
    }
    return render(request, 'tags/tag_new.html', context)

@superuser_required
def tag_edit(request, pk):
    tag = Tag.objects.get(id=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_detail', pk=pk)
    else:
        form = TagForm(instance=tag)
    context = {
        'tag': tag,
        'form': form,
        'title': 'Editar Tag'
    }
    return render(request, 'tags/tag_edit.html', context)

@superuser_required
def tag_list(request):
    template_name = 'tags/tag_list.html'
    tags = Tag.objects.all().order_by('-created_at')
    context = {
        'tags': tags,
        'title': 'Tags'
    }
    return render(request, template_name, context)

@superuser_required
def tag_detail(request, pk):
    template_name = 'tags/tag_detail.html'
    tag = get_object_or_404(Tag, pk=pk)
    context = {
        'tag': tag,
        'title': 'Detalles del Tag'
    }
    return render(request, template_name, context)

@superuser_required
def tag_delete(request, pk):
    tag = Tag.objects.get(pk=pk)
    tag.delete()
    return redirect('tag_list')








@superuser_required
def product_list(request):
    template_name = 'products/product_list.html'
    products = Article.objects.all().order_by('-created_at')
    context = {
        'products': products
    }
    return render(request, template_name, context)