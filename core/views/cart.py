from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from core.models.customer import Customer
from django.views import  View
from core.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'core/cart.html' , {'products' : products} )
