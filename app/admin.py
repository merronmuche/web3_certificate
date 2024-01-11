
from django.contrib import admin

from app.models import Trainee

class TraineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    

admin.site.register(Trainee, TraineeAdmin)
