from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    account_number=models.BigIntegerField(unique=True)

class Account(models.Model):
    ACCOUNT_TYPE=[
        ('savings','Savings'),
        ('current','Current'),
    ]   
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    account_type=models.CharField(max_length=100,choices=ACCOUNT_TYPE) 
    balance=models.DecimalField(default=0.0,max_digits=12,decimal_places=3)
    account_number = models.BigIntegerField(primary_key=True)

class Transaction(models.Model):
    TRANSACTION_TYPE=[
        ('Debit','debit'),
        ('Credit','credit'),
        
    ]
    user=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='account')
    transaction_type=models.CharField(max_length=50,choices=TRANSACTION_TYPE)
    date=models.DateTimeField(auto_now=True)
    amount=models.DecimalField(max_digits=12,decimal_places=3)
  
   

