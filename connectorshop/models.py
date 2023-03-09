from django.contrib.auth.models import User, Permission
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class userDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', default='avatar/notuser.jpg')

class Message(models.Model):
    text = models.CharField(max_length=200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/')
    highlighted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    highlighted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, default='0')
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/nullproduct.jpg')
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.sku
    
class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
