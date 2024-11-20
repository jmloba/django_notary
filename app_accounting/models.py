from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

#validators
from app_accounts.utils import regex_validators_alpha


#validators
numeric_char = RegexValidator(r"^[0-9]+$", 'only numbers are allowed')

alphanumeric = RegexValidator(r"^[a-z\d\-_\s]+$", 'Alphanumeric')

alpha_only = RegexValidator(r"^[a-zA-Z\- ]*$", 'Alpha only')

mobile_format = RegexValidator(r"^\d\d\d\d\d\d\d\d\d\d\d$", 'Format : 11 digits')

class myvalidator(models.Model):  
  val_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True) 

  name = models.CharField(
    max_length=50,  
    null=True,
    unique=False,
    validators=[regex_validators_alpha()],
    # help_text=("format:9999-999-9999,required,unique"),
    verbose_name='Name'
    )

  mobile_no = models.CharField(
    max_length=13,  
    unique=True, null=True,
    validators=[mobile_format],
    # help_text=("format:9999-999-9999,required,unique"),
    verbose_name='Mobile Number'
    )
  
  birth_date = models.DateField(
    null=True,
    verbose_name='Date of Birth'
    )
  place_birth = models.CharField(  
    null=True,
    verbose_name='Place of Birth' 
  )
  
  class Meta:
    verbose_name_plural= 'Sample VAlidator File'   

  def __str__(self) -> str:
        return self.birth_date.strftime('%d/%m/%Y')   
  
class chart_acct(models.Model):
  class HeaderChoices(models.TextChoices):
     Header = 'H'
     Detail = 'D'

  chrt_accno = models.CharField(
    max_length=10,   null=True, blank=True, unique=True
   )
  chrt_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,) 
  chrt_desc = models.CharField(max_length=200, blank=True, null=True)  

  chrt_H_D = models.CharField(max_length=1, choices=HeaderChoices.choices, blank=True, null=True)  


  chrt_curr = models.CharField(max_length=3, blank=True, null=True)   
  beg_bal = models.DecimalField(max_digits=13, decimal_places=2, default=0, blank=True, null=True)  
  date_last_movement = models.DateTimeField( null=True)   

  date_created = models.DateTimeField(auto_now_add=True, null=True)   

  @property
  @admin.display(description='beg_bal', ordering='beg_bal')
  def beg_bal_formatted(self):
    return f'{self.beg_bal:,}'  
  
  def __str__(self):
        # return str(self.chrt_accno+' '+self.chrt_desc    )
        return str(self.chrt_accno)
  
  def str_accno(self):
        return str(self.chrt_accno)
  class Meta:
    verbose_name_plural= 'Chart of Accounts'   

class voucher_creation(models.Model):  
  accno = models.ForeignKey(chart_acct, on_delete=models.CASCADE, null=False)  
  author = models.ForeignKey(User,default=None,on_delete=models.CASCADE, )
  voucher_group =models.IntegerField(default=0)
  dc = models.CharField(max_length=1, blank=True, null=True)
 
  class Meta:
    verbose_name_plural= 'Voucher'     
    
  @property  # read field from another table's field
  def acct_name(self):
     return self.accno.chrt_desc    

# this table is for testing  = CreateVoucherGroup
class CreateVoucherGroup(models.Model):
  accno = models.ForeignKey(chart_acct, on_delete=models.CASCADE, null=True, blank=True) 
  desc = models.CharField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateField(auto_now_add=True)
  class Meta:
    verbose_name_plural= 'Create Voucher Group -orm'     

  @property 
  def acct_name(self): # read field from another table's field
     return self.accno.chrt_desc


class ytdfd(models.Model):
  
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   
  voucherno =  models.IntegerField(default=0)
  voucher_date = models.DateField(blank=True, null=True)
  accno = models.ForeignKey(chart_acct, on_delete=models.SET_NULL, null=True)   

  dr = models.CharField(max_length=10, blank=True, null=True)
  amount = models.DecimalField(max_digits=13, decimal_places=2, default=0, blank=True, )
  project = models.CharField(max_length=10, blank=True, null=True)


  date_created = models.DateTimeField(auto_now_add=True, null=True)   
  class Meta:
    verbose_name_plural= 'YTDFD'     
class currency(models.Model):
  curr = models.CharField(max_length=3, blank=True, null=True)
  curr_desc  = models.CharField(max_length=100, blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)  
  class Meta:
    verbose_name_plural= 'Currency'     


