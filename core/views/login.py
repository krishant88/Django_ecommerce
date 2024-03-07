
from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from core.models.customer import Customer
from django.views import  View


class Login(View):
    def get(self, request):
          return render(request, 'core/login.html')
    
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        customers = Customer.objects.filter(email=email)

        error_message = None

        if customers.exists():
            for customer in customers:
                flag = check_password(password, customer.password)

                if flag:
                    request.session['customer']=customer.id
                    
                    return redirect('core:homepage')
                    
                
                else:
                    error_message = 'Email or password is incorrect'
        else:
            error_message = 'Email or password is incorrect'

        return render(request, 'core/login.html', {'error': error_message})
     
        

def logout(request):
    request.session.clear()
    return redirect('core:login')
