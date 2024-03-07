from django.db import  models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(default="",null=True)
    password = models.CharField(max_length=500,null=True)

   

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.get(email = self.email):
            return True

        return  False

