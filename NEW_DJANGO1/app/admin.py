from .models import *
from django.contrib.auth.admin import *
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(SessionTime)
admin.site.register(Student)
