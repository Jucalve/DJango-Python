from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'), #Here is where my diferet paths will be taken
                                         #like /download. /info, etc.
                                         #the actual HTML page is in views in the function 'index'
    path('something', views.something, name='something'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index2')
]