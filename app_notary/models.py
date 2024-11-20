from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator

# Create your models here.
class posted_transaction(models.Model):
  Posted_key= models.CharField(max_length=30, blank=True, null=True)
  date_posted = models.DateTimeField(auto_now=True,null=True)

class File_Serials(models.Model) :
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
  serial_name =  models.CharField(max_length=30, blank=True, null=True)
  next_serial_number = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(100000)])
  def __str__(self):
    return self.serial_name
  
  
class Notary_Category(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
  doc_category = models.CharField(max_length=200)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateField(auto_now_add=True)
  class Meta:
    verbose_name_plural= 'Notary Categories'     
  def __str__(self):
    return str(self.doc_category)
  
  @property
  def my_username(self):
    return self.user.username

  

  
class Notarized_Documents(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
  category = models.ForeignKey(Notary_Category,on_delete=models.PROTECT, null=True, blank=True)
  firstname = models.CharField(max_length=30, blank=True, null=True)
  lastname = models.CharField(max_length=30, blank=True, null=True)
  address = models.CharField(max_length=200, blank=True, null=True)

  bookno = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
        )
  pageno = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(2000)])
  recordno = models.IntegerField( blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(50)])
  

  myimage = models.ImageField(upload_to='myimages/', null=True,blank=True)

  myfile = models.FileField(upload_to='myfiles/', null=True, blank=True)

  amount = models.DecimalField( max_digits=7,decimal_places=2, blank=True, null=True)
  

  tax_data= models.JSONField(blank=True, null = True, help_text="Data format:{'tax_type':{'tax_percentage':'tax_amount'}}")

#   total_tax = models.FloatField(default=0, null=True, blank=True)
  total_tax_amount = models.FloatField(default=0, null=True, blank=True)

  total_data =models.JSONField(blank=True, null = True, help_text="Data format : {'tax_type'}:{'tax_percentage': {tax_amount}}")
  total_amount =models.DecimalField( max_digits=10,decimal_places=2, blank=True, null=True) 

  updated = models.DateTimeField(auto_now=True,null=True)
  created = models.DateField(auto_now_add=True,null=True)

  posted_serial= models.CharField(max_length=30, blank=True, null=True)
  is_posted= models.BooleanField(default = False)  
  date_posted = models.DateTimeField(null=True, blank=True)  
  or_number =   models.CharField(max_length=30, blank=True, null=True)

  
  class Meta:
    verbose_name_plural= 'Notarized Documents'     

  def __str__(self):
    return str(self.firstname)  
    
class Notary_Posting (models.Model) :
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
 
  posted_serial= models.CharField(max_length=30, blank=True, null=True)
  amount = models.DecimalField( max_digits=10,decimal_places=2, blank=True, null=True) 

  tax = models.DecimalField( max_digits=10,decimal_places=2, blank=True, null=True)     
  total_amount = models.DecimalField( max_digits=10,decimal_places=2, blank=True, null=True) 