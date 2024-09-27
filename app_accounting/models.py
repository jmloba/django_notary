from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator


# Create your models here.
class currency(models.Model):
  curr = models.CharField(max_length=3, blank=True, null=True)
  curr_desc  = models.CharField(max_length=100, blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)  


class chart_acct(models.Model):
  chrt_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
  chrt_accno = models.CharField(max_length=10, blank=True, null=True)
  chrt_desc = models.CharField(max_length=200, blank=True, null=True)  
  chrt_H_D = models.CharField(max_length=1, blank=True, null=True)  
  chrt_curr = models.CharField(max_length=3, blank=True, null=True)   
  beg_bal = models.DecimalField(max_digits=13, decimal_places=2, default=0, blank=True, null=True)  
  date_last_movement = models.DateTimeField( null=True)   

  date_created = models.DateTimeField(auto_now_add=True, null=True)   

  @property
  @admin.display(description='beg_bal', ordering='beg_bal')
  def beg_bal_formatted(self):
    return f'{self.beg_bal:,}'  
  
class ytdfd(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   
  voucherno =  models.IntegerField(default=0)
  voucher_date = models.DateField(blank=True, null=True)
  accno = models.ForeignKey(chart_acct, on_delete=models.SET_NULL, null=True)   

  dr = models.CharField(max_length=10, blank=True, null=True)
  amount = models.DecimalField(max_digits=13, decimal_places=2, default=0, blank=True, )
  project = models.CharField(max_length=10, blank=True, null=True)


