from http.client import ResponseNotReady
from urllib import request, response
from wsgiref.validate import validator
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer, ValidationError
from django.core.validators import validate_email as dj_validate_email
from django.db.models import Q
from django.utils.translation import gettext as _ 
from rest_framework.fields import *
from rest_framework import serializers
from .models.implementation import Wallet, WalletTransaction

import requests

User = get_user_model()

class DepositInputSerializer(Serializer):
    
    amount = serializers.IntegerField(validators=[is_amount])
    email = serializers.EmailField()
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            return value
        raise serializers.ValidationError({"detail": "Email not found"})
    
    def save(self):
        user = self.context['request'].user
        wallet = Wallet.objects.get(user=user)
        data = self.validated_data
        url = 'https://api.paystack.co/transaction/initialize'
        headers = {
            {"authourization": f"Bearier {settings.PAYSTACK_SECRET_KEY}"}
            
        }
        
        r = requests.post(url, headers=headers, data=data)
        response = r.json()
        
        WalletTransaction.objects.create(
            wallet=wallet,
            transaction_type='deposit',
            amount=data['amount'],
            paystack_payment_reference=response['data']['reference'],
            status='pending',
        )
        
        return response