# from asyncio.log import logger
import logging
import traceback
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
from core.model_serializer import (
    BalanceSerializer,
    UserSerializer,
)
from .input_serializers import SigninInputSerializer
from .responses_serialisers import (
    EmptySerializer,
    NotFoundResponseSerializer,
    BadRequestResponseSerializer,
    
)
from .responses import (
    BadRequestResponse,
    CreatedResponse,
    GoodResponse,
    
)
from rest_framework import permissions
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model 
from rest_framework.authtoken.models import Token

logger = logging.getLogger()
User = get_user_model()

class RegisterViewset(YkGenericViewSet):

    @swagger_auto_schema(
        operation_summary="signup",
        operation_description="Signup ",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=RegisterSerializer(),
    )
    
    @action(methods=["POST"], detail=False, authentication_classes = (), permission_classes = ())
    
    def signup(self, request, *args, **kwargs):
        try:
                
            rcv_ser = RegisterSerializer(data=self.request.data)
            if rcv_ser.is_valid(raise_exception=True):
                password = rcv_ser.validated_data.pop('password', None)
                user = User.objects.create(**rcv_ser.validated_data)
                user.set_password(password)
                user.save()
                Token.objects.create(user=user)
                
                return GoodResponse(rcv_ser.data)
                #return CreatedResponse({"message": "user created"})
            
        except Exception as e:
            logger.error(traceback.print_exc())
            return BadRequestResponse(str(e), code="unknown", request=self.request)



class BalanceViewset(YkGenericViewSet):
    
    def get_queryset(self):
        return User.objects.filter(email=self.request.user)
    
    @swagger_auto_schema(
        operation_summary="Transer",
        operation_description="Transfer any amount",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=BalanceSerializer(),
    )
    
    @action(methods=["POST"], detail=False, permission_classes=[permissions.IsAuthenticated])
    
    def create_(self, request, *args, **kwargs):
        transf_ser = BalanceSerializer(data=self.request.data)
        print(transf_ser)    
            
            
class LoginViewset(YkGenericViewSet):
    @swagger_auto_schema(
        operation_summary="login",
        operation_description="login",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        request_body=SigninInputSerializer(),
        
    )
    
    @action(methods=["POST"],  detail=False)
    
    def post(self, request, *args, **kwags):
        rcv_ser = SigninInputSerializer(data=self.request.data)
        
        if rcv_ser.is_valid():
            print(rcv_ser)
    