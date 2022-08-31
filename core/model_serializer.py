from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer 
from rest_framework.serializers import CharField, IntegerField, ListSerializer




User = get_user_model()


class UserSerializer(ModelSerializer):
    id = IntegerField()
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "date_joined", "is_active", "account_balance")
        
        
class BalanceSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ("account_balance") 
    