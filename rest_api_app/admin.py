from django.contrib import admin
from rest_api_app.models import Techie


class TechieAdmin(admin.ModelAdmin):
    list_display = ('techie_id', 'techie_name', 'techie_profile', 'techie_salary', 'techie_skill')
    list_display_links = ('techie_name', 'techie_profile', 'techie_salary')


admin.site.register(Techie, TechieAdmin)
