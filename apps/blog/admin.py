from django.contrib import admin
from django.contrib.admin import options

options

# Register your models here.
from django_manager import admin as manager_admin
manager_admin.registers(editor_md_fields=('body',))

