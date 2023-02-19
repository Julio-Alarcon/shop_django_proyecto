from django.urls import path
from . import views
from .views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('products/', views.products, name='products'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('user_edit/', views.user_edit, name='user_edit'),
    
    path('tag/list/', views.tag_list, name='tag_list'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('tag/new/', views.tag_new, name='tag_new'),
    path('tag/<int:pk>/edit/', views.tag_edit, name='tag_edit'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
    
    path('category/list/', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    path('product/list/', views.product_list, name='product_list'),
]