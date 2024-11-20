from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

#validators
from app_accounts.utils import regex_validators_alpha,regex_validators_numberonly,regex_validators_alphanumeric,regex_validators_philmobile,regex_validators_xx


class StudentRec(models.Model):
  studno = models.CharField(max_length=10, null=True, blank=True, unique=True,
     validators=[regex_validators_numberonly()],                        )

  firstname= models.CharField(max_length=50, 
    null = True, blank=True, 
    validators=[regex_validators_alphanumeric()],
    )

  lastname= models.CharField(max_length=50, 
    null = True, blank=True,
    validators=[regex_validators_alpha()],)
  birthdate= models.DateField( null = True, blank=True)

  mobile=models.CharField(max_length=30, null=True, blank=True,
      verbose_name='Mobile Number', 
       validators=[regex_validators_philmobile()],
      unique=True )
  
  notes=models.CharField(max_length=2000, null=True,blank=True,validators=[ regex_validators_alphanumeric()]
            )
                         
  date_created = models.DateTimeField(auto_now_add=True, null=True)   

  def __str__(self):
        # return str(self.chrt_accno+' '+self.chrt_desc    )
        return str(self.firstname+' '+self.lastname)
  class Meta:
    verbose_name_plural= 'Student Rec'   
  
  
