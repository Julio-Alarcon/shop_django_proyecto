from django import forms
from .models import Category, Article, Tag, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

## FORMULARIO DE INICIO DE SESION ##


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

## FORMULARIO DE REGISTRO ##


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password
## FORMULARIO DE REGISTRO ##


## FORMULARIO DE EDICCION DE DATOS DEL USUARIO ##
class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
## FORMULARIO DE EDICCION DE DATOS DEL USUARIO ##


## FORMULARIO DE EDICCION DE CONTRASEÑA DEL USUARIO ##
class EditPasswordForm(PasswordChangeForm):
    pass
## FORMULARIO DE EDICCION DE CONTRASEÑA DEL USUARIO ##


## FORMULARIO DE CREACION Y EDICCION DE CATEGORIAS ##
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image', 'highlighted', 'order']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'highlighted': 'Destacado',
            'order': 'Orden',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'highlighted': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'})
        }
## FORMULARIO DE CREACION Y EDICCION DE CATEGORIAS ##


## FORMULARIO DE CREACION Y EDICCION DE CATEGORIAS ##
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description', 'highlighted', 'order']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'highlighted': 'Destacado',
            'order': 'Orden',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'highlighted': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'})
        }
## FORMULARIO DE CREACION Y EDICCION DE CATEGORIAS ##


## FORMULARIO DE CREACION Y EDICCION DE ARTICULOS ##
class ArticleForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=forms.SelectMultiple)
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Article
        fields = ['title', 'sku', 'price', 'stock', 'description',
                  'image', 'category', 'tag', 'published']
## FORMULARIO DE CREACION Y EDICCION DE ARTICULOS ##


## FORMULARIO DE BUSQUEDA DE ARTICULOS ##
class ArticleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Buscar...'}))
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(
    ), widget=forms.CheckboxSelectMultiple, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), empty_label='Seleccionar categoría', required=False)

    def search_articles(self):
        search_text = self.cleaned_data['search']
        tag = self.cleaned_data['tag']
        category = self.cleaned_data['category']
        articles = Article.objects.all()
        if search_text:
            articles = articles.filter(title__icontains=search_text)
        if tag:
            articles = articles.filter(tag__in=tag)
        if category:
            articles = articles.filter(category=category)
        return articles
## FORMULARIO DE BUSQUEDA DE ARTICULOS ##


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES)
    article_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Review
        exclude = ('author',)

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'rating': 'Calificación',
            'comment': 'Comentario',
        }

    def __init__(self, *args, **kwargs):
        article_id = kwargs.pop('article_id', None)
        super().__init__(*args, **kwargs)
        self.fields['article_id'].initial = article_id

    def save(self, commit=True):
        review = super().save(commit=False)
        review.article_id = self.cleaned_data['article_id']
        review.author_id = self.initial['author'].id
        review.save()
        return review
