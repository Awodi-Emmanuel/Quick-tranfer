from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer 
from rest_framework.serializers import CharField, IntegerField, ListSerializer
from rest_framework.authtoken.models import Token




User = get_user_model()


class UserSerializer(ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password", "date_joined", "is_active")
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user    
        
        
# class BalanceSerializer(ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ("account_balance") 
    