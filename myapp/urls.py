from django.urls import path
from . views import Userprofileview,Userprofileeditview,Userregisterationview,Transactioncreateview,Accountcreateview,Accountupdateview
urlpatterns=[
    path('register/',Userregisterationview.as_view()),
    path('userprofile/',Userprofileview.as_view()),
    path('userprofile/<int:user>/',Userprofileeditview.as_view()),
    path('account/',Accountcreateview.as_view()),
    path('account/<int:pk>/',Accountupdateview.as_view()),
    path('transactions/',Transactioncreateview.as_view()),
  
]