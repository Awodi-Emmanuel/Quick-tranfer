# from asyncio.log import logger
import logging

from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
)
from core.custom_classes import YkGenericViewSet
from core.custom_classes import YkGenericViewSet
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from core.input_serializers import RegisterSerializer 
from core.model_serializer import UserSerializer

from core.responses_serialisers import (
    EmptySerializer,
    NotFoundResponseSerializer,
    BadRequestResponseSerializer,
    
)
from core.responses import (
    BadRequestResponse,
    CreatedResponse,
    GoodResponse,
    
)


from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model 


from rest_framework import status
from django.conf import settings
from .model_serializer import WalletSerializer, DepositSerializer
from .models.implementation import Wallet, WalletTransaction

logger = logging.getLogger()
User = get_user_model()

class WalletViewset(YkGenericViewSet):
    
    def get_queryset(self):
        return User.objects.filter(email=self.request.user)
    
    @swagger_auto_schema(
        operation_summary="Wallet",
        operation_description="Transfer any amount",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        # request_body=WalletSerializer(),
    )
    
    @action(methods=["GET"], detail=False, url_path="wallet")
    
    def wallet_info(self, request):
        try:
                
            wallet_ser = WalletSerializer(data=self.request.data)
            print(wallet_ser)
            if wallet_ser:
                wallet = Wallet.objects.get(user=request.user)
                data = WalletSerializer(wallet).data
                
                return GoodResponse({"data": data})
        except Exception as e:
            return BadRequestResponse(str(e), "Unknown", request=self.request)
        
        
        
    @swagger_auto_schema(
        operation_summary="Deposit",
        operation_description="Deposit some fund",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=DepositSerializer(),
    )
    
    @action(methods=["POST"], detail=False,)
    
    def deposit(self, request, *args, **kwargs):
        rcv_ser = DepositSerializer(data=self.request.data)
        if rcv_ser.is_valid(raise_exception=True):
            print(rcv_ser) 
           