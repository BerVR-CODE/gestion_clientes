from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Order  (models.Model):
     order_number = models.CharField(max_length=100)
     order_date = models.DateField()
     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
     def __str__(self):
            return f"Order {self.order_number} - {self.customer.first_name} {self.customer.last_name}"