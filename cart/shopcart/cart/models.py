from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class userregistration(models.Model):
    
    id         = models.AutoField(primary_key=True)
    Name       = models.CharField(max_length=50)
    Mobile     = models.CharField(max_length=10)
    Email      = models.EmailField(max_length=254)
    Password   = models.CharField(max_length=500)
    Address    = models.CharField(max_length=500)
    State      = models.CharField(max_length=500)
    Country    = models.CharField(max_length=500)

    class Meta:
        db_table='userregistration'

 
    
    
    
class login(models.Model):
    id       = models.AutoField(primary_key=True)
    Email    = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'login'

    
    
    

class Grocery(models.Model):
    id          = models.AutoField(primary_key=True)
    product   = models.CharField(max_length=200)
    amount = models.IntegerField()
    image = models.ImageField(upload_to="image")
    

    class Meta:
        db_table = 'Grocery'
        
        
        
# class Cart(models.Model):
#     user = models.ForeignKey(login, on_delete=models.CASCADE,default=1)
#     product = models.ForeignKey(Grocery, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} for {self.user.username}"
    
    
        
class Carts(models.Model):
    
    product = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"