from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

    
class Phil_City (models.Model) :

  country =models.CharField(max_length=80,  blank=False, null=False)
  city = models.CharField(max_length=50, blank=False, null=False)
  province = models.CharField(max_length=50, blank=False, null=False)
  is_active = models.BooleanField(default=True)
  
  created_at = models.DateTimeField(default=datetime.now, blank=True)

class Phil_Province_Towns (models.Model) :

  country =models.CharField(max_length=80,  blank=False, null=False)
  towns = models.CharField(max_length=50, blank=False, null=False)
  province = models.CharField(max_length=50, blank=False, null=False)

  municipal_class = models.CharField(max_length=50, blank=False, null=False)

  barangay_no = models.IntegerField(default=0,blank=False, null=False)
  is_active = models.BooleanField(default=True)
  
  created_at = models.DateTimeField(default=datetime.now, blank=True)




  

