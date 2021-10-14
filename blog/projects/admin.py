from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','password','created_date','balance')
    list_filter = ('created_date',)
    list_editable = ('first_name',)
    search_fields = ('id','last_name')
    list_per_page = 20
# Register your models here.
admin.site.register(Customer,CustomerAdmin)