from django.contrib import admin

# Register your models here.
from .models.implementation import (
    Wallet,
    WalletTransaction
)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    pass