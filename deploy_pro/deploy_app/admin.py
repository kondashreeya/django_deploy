from django.contrib import admin
from deploy_app.models import employee
# Register your models here.
class emp_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_salary']
admin.site.register(employee,emp_admin)