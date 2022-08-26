from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer 
from rest_framework.serializers import CharField, IntegerField, ListSerializer




User = get_user_model()


class ModelSerializer(ModelSerializer):
    id = IntegerField()
    
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "date_joined", "is_active", "account_balance")
    