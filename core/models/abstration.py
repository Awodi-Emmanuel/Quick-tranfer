from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import gettext as _
from django.core.mail import send_mail




class Users(AbstractBaseUser):
    email: models.EmailField = models.EmailField(_('email address'), unique=True)
    first_name: models.CharField = models.CharField(_('first name'), max_length=30, blank=True)
    last_name: models.CharField = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined: models.DateTimeField = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active: models.BooleanField = models.BooleanField(_('active'), default=True)
    account_balance: models.DecimalField = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
    
    objects = UserManager() 
    REQUIRED_FIELDS = [
        'email'
    ]
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True 
        # USERNAME_FIELD = 'email'
        # REQUIRED_FIELDS = []
        
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        '''
        Returns the short name for the user
        '''
        return self.first_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
     
        # verbose = _('user')
        # verbose_name_plural = _('users')
        
        
