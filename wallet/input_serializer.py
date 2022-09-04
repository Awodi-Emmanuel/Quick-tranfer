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

