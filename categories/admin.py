from django.contrib import admin
from categories.models import Discipline, Industry

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    pass
