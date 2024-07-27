from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
  amount = models.FloatField(blank = True, null=True)
  date = models.DateField(default=now)
  description = models.TextField(default = '', blank = True, null=True)
  owner = models.ForeignKey(to = User, on_delete=models.CASCADE,blank = True, null=True)
  category= models.CharField(max_length = 255,blank = True, null=True)

  posted = models.BooleanField(default=False)
  posted_by = models.ForeignKey(User, on_delete=models.PROTECT,blank = True, null=True ,related_name='postedby_expense')
  posted_date=models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.category

class  Category(models.Model) :
    
    name = models.CharField(max_length=255)
    class Meta:
       verbose_name_plural='Categories'
    def __str__(self):
       return self.name
       
