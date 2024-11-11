from .models import Account,Userprofile,Transaction
from rest_framework import serializers
from django.contrib.auth.models import User

class Registerationserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']


class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model=Userprofile
        fields=('__all__')

class Accountserializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=('__all__')

class Transactionserializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=('__all__')            