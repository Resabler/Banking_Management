from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import Registerationserializer,Transactionserializer,Userprofileserializer,Accountserializer
from .models import Transaction,Userprofile,Account
from rest_framework.permissions import IsAuthenticated

class Userregisterationview(APIView):
    def post(self,request):
        serializer=Registerationserializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            access_token=AccessToken.for_user(user)
            return JsonResponse({"message":"User creation is successful","your token":str(access_token),"user_id":user.id})
        return JsonResponse({"error":"An error has been occurred.","details":serializer.errors},status=400)
    
class Userprofileview(generics.ListCreateAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=Userprofileserializer
    permission_classes=[ IsAuthenticated]

class Userprofileeditview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Userprofile.objects.all()
    serializer_class=Userprofileserializer 
    lookup_field = 'user' 
    permission_classes=[ IsAuthenticated]

class Transactioncreateview(generics.ListCreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=Transactionserializer
    lookup_field = 'user' 
    permission_classes=[ IsAuthenticated]

class Accountcreateview(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=Accountserializer
    permission_classes=[ IsAuthenticated]


class Accountupdateview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=Accountserializer
    permission_classes=[ IsAuthenticated]
   



