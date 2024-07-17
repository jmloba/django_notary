from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator

# Create your models here.

class Notary_Category(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
  doc_category = models.CharField(max_length=200)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateField(auto_now_add=True)

  def __str__(self):
    return str(self.doc_category)
  
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

  amount_paid = models.DecimalField( max_digits=7,decimal_places=2, blank=True, null=True)
  updated = models.DateTimeField(auto_now=True,null=True)
  created = models.DateField(auto_now_add=True,null=True)
  def __str__(self):
    return str(self.firstname)  
    