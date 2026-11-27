from django.contrib import admin
from .models import *
admin.site.site_header='HORIZON SIS Administration'
admin.site.site_title='HORIZON SIS'
admin.site.index_title='School operations'
for model in [SchoolClass,Subject,Student,StaffMember,ParentProfile,Attendance,Exam,Result,Fee,Payment,TimetableEntry]:
    admin.site.register(model)
