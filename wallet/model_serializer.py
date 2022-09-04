from dataclasses import field
from locale import currency
from .models.implementation import Wallet, WalletTransaction
from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer 
from django.db.models import Sum
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from django.conf import settings
import requests

class WalletSerializer(serializers.ModelSerializer):
    """
    Serializer to valid the user's wallet
    
    """
    
    balance = serializers.SerializerMethodField()
    
    def get_balance(self, obj):
        bal = WalletTransaction.objects.filter(
            Wallet=obj, status="success").aggregate(Sum('amount'))['amount__sum']
        return bal
    
    class Meta:
        model = Wallet
        fields = ['id', 'currency',  'balance']
        
def is_amount(value):
    if value <= 0:
        raise serializers.ValidationError({"detail": "Invalid Amount"})
    return value


