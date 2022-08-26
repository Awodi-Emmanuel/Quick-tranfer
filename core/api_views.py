from ast import operator
from crypt import methods
from http.client import responses
from urllib import response
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
)
from core.custom_classes import YkGenericViewSet
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from core.input_serializers import RegisterSerializer
from .responses_serialisers import (
    EmptySerializer,
    NotFoundResponseSerializer,
    BadRequestResponseSerializer,
    
)
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema


class RegisterViewset():
    
    @swagger_auto_schema(
        operation_summary="signup",
        operation_description="Signup ",
        responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
        requets_body=RegisterSerializer(),
    )
    
    @action(methods=["POST"], detail=False)
    
    def signup(self, request, *args, **kwargs):
        rcv_ser = RegisterSerializer(data=self.request.data)
        print(rcv_ser)