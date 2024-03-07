from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from core.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
         postData = request.POST
         first_name = postData.get('firstname')
         last_name = postData.get('lastname')
         phone = postData.get('phone')
         email= postData.get('email')
         password =postData.get('password' )

         customer= Customer(first_name= first_name,
                            last_name= last_name,
                            phone=phone,
                            email=email,
                            password= password)
         
         print("Values from form:", first_name, last_name, phone, email, password)
          
         customer.password =make_password(customer.password)
         customer.save()
         return redirect('core:homepage')

