from django.contrib import admin
from .models import UserAccount
from . import models

class SKMSAdminData(admin.AdminSite):
    site_header = 'SKMS User Admin Info'

skms_admin_site = SKMSAdminData(name='SKMSAdmin')

skms_admin_site.register(models.UserAccount)

skms_admin_site.site_url = "/skms/index/"
