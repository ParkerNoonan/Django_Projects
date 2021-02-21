from django.contrib import admin
from .models import Project, Valves, Actuator, Torque_Table, City_County_Temp

# Register your models here.
admin.site.register(Project)
admin.site.register(Valves)
admin.site.register(Actuator)
admin.site.register(Torque_Table)
admin.site.register(City_County_Temp)