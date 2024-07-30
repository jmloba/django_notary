from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime


# Create your models here.
class Ref_Table (models.Model):
  reference = models.CharField(max_length=20, blank=True, null=True)
  ref_no = models.IntegerField(default=0,blank=True, null=True)
  def __str__(self):
    return self.reference
  
class Customer(models.Model)  :
  user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
  name=models.CharField(max_length=200, null=True)
  phone=models.CharField(max_length=200, null=True)
  email=models.CharField(max_length=200, null=True)
  profile_pic = models.ImageField(default='profile.png',null=True,blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
    return str(self.name)
  
       
class Invoice (models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)                         
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)

  invoice_no = models.IntegerField(default=0, blank=True, 
                                 null=True)

  invoice_date  = models.DateTimeField(default=datetime.now, blank=True, null=True)
  
  itemnumber = models.CharField(max_length=20, blank=True, null=True)

  description = models.CharField(max_length=50, blank=True, null=True) 
  quantity = models.IntegerField(default=1, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
  def __str__(self):
    return str(self.customer)
  
class InvoiceSummary(models.Model):
  user=  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   

  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)

  invoice_no = models.IntegerField(default=0)

  invoice_date= models.DateTimeField(default=datetime.now, blank=True, null=True)
  
  total_quantity=models.IntegerField(default=0, validators=[
          MaxValueValidator(100),
          MinValueValidator(1) ],blank=True, null=True)
  
  total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)  
  class Meta:
       verbose_name_plural='InvoiceSummary'    
  def __str__(self):
    return str(self.customer)
class Category_Sales(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)     
  category  = models.CharField(max_length=200, blank=True, null=True) 
