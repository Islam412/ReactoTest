from django.contrib import admin
from userauths.models import User , Account , KYC


# Register your models here.


class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['username', 'email']
    list_filter = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('user_permissions',)


class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance', 'kyc_submitted', 'kyc_confirmed'] 
    list_display = ['user', 'account_number' ,'account_status', 'kyc_submitted', 'kyc_confirmed'] 
    list_filter = ['account_status']
    search_fields = ['user__username', 'user__email', 'account_number']


class KYCAdmin(ImportExportModelAdmin):
    search_fields = ["frist_name" , "last_name" , "account"]
    list_display = ['user', 'frist_name' , "last_name", 'gender', 'date_of_birth'] 


admin.site.register(User, UserCustomAdmin)
admin.site.register(Account, AccountAdminModel)
admin.site.register(KYC, KYCAdmin)