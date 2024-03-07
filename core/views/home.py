from django.shortcuts import render, redirect

from django.http import HttpResponse
from core.models.product import Product
from core.models.category import Category
from core.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.

class Index(View):
     def post(self, request):
         product =request.POST.get('product')
         remove = request.POST.get('remove')
         cart= request.session.get('cart')
         if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
         else:
            cart = {}
            cart[product] = 1

         request.session['cart'] = cart
         print('cart' , request.session['cart'])
         return redirect('core:homepage')
         

     def get(self, request):
        products= None
        
    # return render(request, 'orders/order.html' )
        categories = Category.get_all_categories();
        categoryID = request.GET.get('category')
        if categoryID:
          products=Product.get_all_products_by_categoryid(categoryID);
        else:
         products=Product.get_all_products();

    
        data={}
        data['products'] = products
        data['categories'] = categories
        print("you are :" ,request.session.get('email'))
        return render(request, 'core/index.html', data)


     

    


        
def aboutus(request):
     return render(request, 'core/aboutus.html')

def faq(request):
     return render(request,'core/faq.html')