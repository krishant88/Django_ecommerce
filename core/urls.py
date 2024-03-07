from django.contrib import admin
from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login 
from .views.login import logout
from .views import home
from .views.cart import Cart

app_name= "core"

urlpatterns= [
    path("", Index.as_view(), name='homepage' ),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('index', home.Index.as_view()),
    path('aboutus',home.aboutus),
    path('faq',home.faq),
     path('cart', Cart.as_view() , name='cart'),
]

