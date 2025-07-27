from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('readers/', views.readers_tab, name='readers'),
    path('bag/', views.bag, name='bag'),
    path('returns/', views.returns, name='returns'),
    path('books/', views.books, name='books'),
    path('save_reader', views.save_reader, name='save_reader'),

]
