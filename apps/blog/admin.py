from django.contrib import admin

# Register your models here.
from django_manager import admin as manager_admin
manager_admin.registers(editor_md_fields=('change_message',))
