from django.contrib import admin
from .models import users,subject,question,result
# Register your models here.

# class user_details_admin(admin.ModelAdmin):
#     list_display=('Email','faculty_id')#,'DOB')

# class patent_details_admin(admin.ModelAdmin):
    # list_display=('','faculty_Id')

        


admin.site.register(users)#,user_details_admin)
admin.site.register(subject)#,patent_details_admin)
admin.site.register(question)
admin.site.register(result)